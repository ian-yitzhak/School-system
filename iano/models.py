from django.db import models




class Post(models.Model):

    Image = models.ImageField()
    Title = models.CharField(max_length = 200)

    Content = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 200)






    def __str__(self):

        return self.Title

class departments(models.Model):

    Image = models.ImageField()
    Title = models.CharField(max_length = 200)

    Content = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 200)






    def __str__(self):

        return self.Title



class teacher(models.Model):

    Image = models.ImageField()
    Title = models.CharField(max_length = 200)

    Content = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 200)






    def __str__(self):

        return self.Title




 class notice(models.Model):

    
    Title = models.CharField(max_length = 200)

    Content = models.CharField(max_length = 1000)
    






    def __str__(self):

        return self.Title



class dept(models.Model):

    Image = models.ImageField()
    Title = models.CharField(max_length = 200)

    Content = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 200)






    def __str__(self):

        return self.Title