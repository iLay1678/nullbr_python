from dataclasses import dataclass
from typing import Optional


@dataclass
class UserInfoResponse:
    """用户信息及配额响应模型"""

    sub_name: str  #: 订阅等级名称
    expires_at: Optional[str]  #: 订阅到期时间，free 用户为 null
    daily_used: int  #: 今日已使用配额
    daily_quota: int  #: 每日配额上限
    monthly_used: int  #: 本月已使用配额
    monthly_quota: int  #: 每月配额上限


@dataclass
class UserRedeemResponse:
    """兑换提示码响应模型"""

    success: bool  #: 兑换是否成功
    message: str  #: 兑换结果描述信息
    sub_name: Optional[str] = None  #: 兑换后的订阅等级名称
    expires_at: Optional[str] = None  #: 兑换后的订阅到期时间
