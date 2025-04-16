from django.conf import settings
from django.db import migrations

def insert_category(apps, schema_editor):
    # 環境に依存する名称の設定ファイルを作成しているため、そこから環境を特定する
    settings_file = settings.SETTINGS_MODULE
    env_name = settings_file.split('.')[-1]

    #環境ごとに処理を分ける
    if env_name == 'devlopment':
        #開発環境での処理
        Category = apps.get_model('inventory', 'Category')
        Category.objects.create(name='開発環境用のカテゴリ', parent_category=None)
    else:
        #ステージング環境や本番環境での処理
        pass

class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0004_dml_insert_category_data_by_model"),
    ]
    operations = [
        migrations.RunPython(insert_category),
    ]