from pyspark.sql import SparkSession, DataFrame

spark = (
    SparkSession.builder
    .master("local")
    .appName("Products and categories")
    .getOrCreate()
)

# Таблица продуктов
products = spark.createDataFrame([
    (1, "Product A"),
    (2, "Product B"),
    (3, "Product C"),
    (4, "Product D"),
], ["product_id", "product_name"])

# Таблица категорий
categories = spark.createDataFrame([
    (1, "Category X"),
    (2, "Category Y"),
    (3, "Category Z"),
], ["category_id", "category_name"])

# Отношение таблиц многое ко многим, поэтому создаем 3 таблицу для их связи
products_categories = spark.createDataFrame([
    (2, 2),
    (3, 1),
    (3, 2),
], ['product_id', 'category_id'])

# Я не совсем понял, нужно создать 2 датафрейма и обхединить их или просто связать две таблица через left join
# Пошел по более эффективному способу

# Саязываем таблицы products и categories через products_categories с помощью left join
# В результате будут как пары "Имя продукта – Имя категории" так и "Имя продукта - NULL", где NULL - отутствие категории
pairs_df: DataFrame = products.join(products_categories, on="product_id", how='left').join(categories, on="category_id", how='left') \
    .select("product_name", "category_name")

pairs_df.show()

spark.stop()
