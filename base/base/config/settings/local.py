"""
開発環境設定
開発者個人の設定を記載
"""

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
# masterブランチでは False に設定すること！
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('WEB_DATABASE_NAME'),
        'USER': env('WEB_DATABASE_USER'),
        'PASSWORD': env('WEB_DATABASE_PASSWORD'),
        'HOST': env('WEB_DATABASE_HOST'),
        'PORT': env('WEB_DATABASE_PORT'),
        'ATOMIC_REQUESTS': False,
    }
}

"""
静的ファイル設定
"""
# アプリケーションに紐付かない静的ファイルの置き場所
# collectstaticコマンド実行済の環境では場合はコメントアウト
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)
# collectstaticコマンド実行時の静的ファイル集約先。
# STATICFILES_DIRS とは別の値を指定する必要あり。
# DEBUG=False時はrunserverの静的ファイル自動配信機能が動作しないため、必須設定
# STATIC_ROOT= os.path.join(BASE_DIR, 'static')

"""
ログ設定
"""
LOGGING = {
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # ローカル開発環境⽤
        'local': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s',
        },
    },
    # ハンドラ
    'handlers': {
        # ファイル出⼒⽤ハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    # ロガー
    'loggers': {
        # ⾃作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django本体が出すログ全般を拾うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 発行されるSQL文を出力するための設定
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

"""
GUIによるデバッグ表示設定
"""
if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }
