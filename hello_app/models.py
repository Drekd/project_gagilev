from django.db import models

class Post(models.Model):
    post = models.CharField("Должность", max_length=50)
    salary = models.IntegerField("Зарплата")
    
    class Meta:
        verbose_name = "Должность" 
        verbose_name_plural = "Должности" 
        ordering = ["salary"] 
        indexes = [
            models.Index(fields=["post"]),
            models.Index(fields=["salary"]),
        ]
       
    def __str__(self): 
        return f"{self.post}"

class Seller(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50, blank=True)
    phone_number = models.CharField("Номер телефона", max_length=11)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField("Фотография", upload_to='sellers/', blank=True, null=True)

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"
        ordering = ["last_name", "first_name", "father_name"]  
        indexes = [
            models.Index(fields=["first_name"]), 
            models.Index(fields=["last_name"]),
            models.Index(fields=["phone_number"])
        ]

    def __str__(self): 
        return f"{self.last_name} {self.first_name}"  

class Categories(models.Model):
    name = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"  
        indexes = [
            models.Index(fields=["name"]),  
        ]

    def __str__(self):  
        return f"{self.name}"

class Car(models.Model):
    name = models.CharField("Название", max_length=50)
    price = models.CharField("Цена", max_length=50)
    equipment = models.CharField("Комплектация", max_length=50)
    colour = models.CharField("Цвет", max_length=11) 
    year = models.IntegerField("Год выпуска", default=2024) 
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField("Фотография", upload_to='cars/', blank=True, null=True)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
        ordering = ["price"]
        indexes = [
            models.Index(fields=["name"]), 
            models.Index(fields=["price"]),
            models.Index(fields=["colour"]),
            models.Index(fields=["year"])
        ]

    def __str__(self):  
        return f"{self.name} {self.price} {self.equipment}"


class Order(models.Model):
    costumer_id = models.ForeignKey('Costumer', on_delete=models.CASCADE)  
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name='Продавец')
    price = models.IntegerField("Цена")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["price"]
        indexes = [
            models.Index(fields=["price"])
        ]

    def __str__(self): 
        return f"{self.price}"

class Costumer(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    father_name = models.CharField("Отчество", max_length=50,blank=True)
    phone_number = models.CharField("Номер телефона", max_length=11)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"
        ordering = ["last_name", "first_name", "father_name"]  
        indexes = [
            models.Index(fields=["first_name"]), 
            models.Index(fields=["last_name"]),
            models.Index(fields=["phone_number"])
        ]

    def __str__(self):  
        return f"{self.last_name} {self.first_name}" 