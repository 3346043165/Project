import requests
import json
from typing import Dict, Any, Optional


class BaseAPI:
    def __init__(self, config_path: str = "api_config.json", data_path: str = "test_data.json"):
        self.session = requests.Session()
        self.config = self._load_config(config_path)
        self.test_data = self._load_config(data_path)
        self.base_url = self.config.get("base_url", "")

    def _load_config(self, file_path: str) -> Dict[str, Any]:
        """加载JSON配置文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise Exception(f"配置文件 {file_path} 未找到")
        except json.JSONDecodeError:
            raise Exception(f"配置文件 {file_path} JSON格式错误")

    def _build_url(self, path: str) -> str:
        """构建完整URL"""
        return f"{self.base_url}{path}"

    def _build_headers(self, api_config: Dict, extra_headers: Dict = None) -> Dict:
        """构建请求头"""
        headers = api_config.get('headers', {}).copy()
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def _replace_placeholders(self, data: Dict, context: Dict = None) -> Dict:
        """替换占位符，如 {token}, {user_id} 等"""
        if not context:
            return data

        if isinstance(data, dict):
            return {k: self._replace_placeholders(v, context) for k, v in data.items()}
        elif isinstance(data, str) and data.startswith('{') and data.endswith('}'):
            key = data[1:-1]
            return context.get(key, data)
        else:
            return data

    def call_api(self,
                 api_name: str,
                 path_params: Dict = None,
                 query_params: Dict = None,
                 request_body: Dict = None,
                 context: Dict = None,
                 **kwargs) -> requests.Response:
        """
        统一调用API的方法

        :param api_name: API配置名称
        :param path_params: 路径参数，用于替换path中的 {placeholder}
        :param query_params: 查询参数
        :param request_body: 请求体数据
        :param context: 上下文数据，用于替换headers和body中的占位符
        :param kwargs: 其他requests参数
        :return: Response对象
        """
        if api_name not in self.config["apis"]:
            raise ValueError(f"API '{api_name}' 未在配置中定义")

        api_config = self.config["apis"][api_name]
        method = api_config["method"]

        # 处理路径参数
        path = api_config["path"]
        if path_params:
            path = path.format(**path_params)

        # 处理headers中的占位符
        headers = self._build_headers(api_config, kwargs.pop('headers', {}))
        if context:
            headers = self._replace_placeholders(headers, context)

        # 处理请求体中的占位符
        if request_body and context:
            request_body = self._replace_placeholders(request_body, context)

        url = self._build_url(path)

        # 根据方法选择参数
        request_kwargs = {
            'headers': headers,
            'params': query_params,
            **kwargs
        }

        if method in ['POST', 'PUT', 'PATCH']:
            request_kwargs['json'] = request_body

        # 发送请求
        response = self.session.request(method, url, **request_kwargs)
        return response

    # 便捷方法
    def login(self, username: str, password: str) -> Dict:
        """登录并返回token"""
        data = {"username": username, "password": password}
        response = self.call_api("login", request_body=data)
        response.raise_for_status()
        result = response.json()
        return result

    def get_test_data(self, data_path: str) -> Any:
        """获取测试数据，支持嵌套路径如 'login_credentials.admin' """
        keys = data_path.split('.')
        data = self.test_data
        for key in keys:
            data = data[key]
        return data


# 使用示例
if __name__ == "__main__":
    api = BaseAPI()

    # 示例1: 登录
    login_result = api.login("test_user", "test123456")
    token = login_result.get("token")

    # 示例2: 获取用户信息（使用路径参数和上下文）
    user_info = api.call_api(
        "get_user",
        path_params={"user_id": 123},
        context={"token": token}
    )
    print(user_info.json())

    # 示例3: 创建酒店订单（使用测试数据）
    order_data = api.get_test_data("hotel_orders.beijing_order")
    order_response = api.call_api(
        "create_hotel_order",
        request_body=order_data,
        context={"token": token}
    )
    print(order_response.status_code)