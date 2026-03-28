import logging


# 基础配置(root logger)
if __name__ == "__main__":
    # DEBUG INFO WARNING ERROR CRITICAL
    logger = logging.basicConfig(level=logging.INFO)

