import logging

# 基础配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

logger.debug("调试信息")
logger.info("程序启动")
logger.warning("数据缺失警告")
logger.error("处理失败", exc_info=True)

