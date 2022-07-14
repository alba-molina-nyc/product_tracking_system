import django_filters
from .models import Job, Memo



class JobFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending' , 'Ascending'),
        ('descending' , 'Descending')
    )
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
    class Meta:
        model = Job
        fields = '__all__'
    
    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)

class MemoFilter(django_filters.FilterSet):
    class Meta: 
        model = Memo
        fields = '__all__'



# class JobFilter(django_filters.FilterSet):
#     CHOICES = (
#         ('ascending' , 'Ascending'),
#         ('descending' , 'Descending')
#     )
#     ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

#     class Meta:
#         model = Job
#         fields = {
#             'order_num' : ['icontains', 'iexact'],
#             'SKU' : ['icontains'],
#             'num_items' : ['icontains'],
#             'num_stones' : ['icontains'],
#             'description_text' : ['icontains'],
#             'setter_name' : [],
#             'created' : ['icontains'],
#             'updated' : ['icontains'],
#         }

#     def filter_by_order(self, queryset, name, value):
#         expression = 'created' if value == 'ascending' else '-created'
#         return queryset.order_by(expression)
    




# this version uses a dictionary to match items that "contain"
# class JobFilter(django_filters.FilterSet):
#     class Meta:
#         model = Job
#         fields = {
#             'order_num' : ['icontains'],
#             'SKU' : ['icontains'],
#             'num_items' : ['icontains'],
#             'num_stones' : ['icontains'],
#             'description_text' : ['icontains'],
#             'created' : ['icontains'],
#             'updated' : ['icontains'],
#         }



# build python class that is going to build filter - this version only shows exact search