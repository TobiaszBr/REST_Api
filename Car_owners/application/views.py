from .models import Owner, Car
from .serializers import OwnerSerializer, CarSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.utils.datastructures import MultiValueDictKeyError


def check_if_queryset_is_empty(queryset, objects, parameter_to_check_input,
                               serializer, *parameter_to_check, many=False):
    if queryset:
        serializer = serializer(queryset, many=many)
        return Response(serializer.data)

    parameters = ' '.join([parameter for parameter in parameter_to_check]).strip()
    return Response(f"There are no {objects} with {parameters}"
                    f" {parameter_to_check_input}")

class OwnerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'surname', 'phone')

    def try_to_get_parameters_from_request(self, request):
        try:
            name = request.GET['name'].title()
        except MultiValueDictKeyError:
            name = ''
        try:
            surname = request.GET['surname'].title()
        except MultiValueDictKeyError:
            surname = ''
        try:
            phone = f"+{request.GET['phone'].strip()}"
        except MultiValueDictKeyError:
            phone = 0

        return name, surname, phone

    # currently function not used
    """def owner_parameters_search_logic(self, name, surname, phone):
        if phone:
            try:
                owners = Owner.objects.get(phone=phone)
            except Owner.DoesNotExist:
                owners = Owner.objects.filter(phone=phone)

            return check_if_queryset_is_empty(owners, 'owners',
                                              'phone',
                                              self.get_serializer,
                                              phone,
                                              many=False)

        elif name and surname:
            owners = Owner.objects.filter(name=name, surname=surname)
            return check_if_queryset_is_empty(owners, 'owners',
                                              'name and surname',
                                              self.get_serializer,
                                              *[name, surname], many=True)

        elif name:
            owners = Owner.objects.filter(name=name)
            return check_if_queryset_is_empty(owners, 'owners', 'name',
                                              self.get_serializer, name,
                                              many=True)

        elif surname:
            owners = Owner.objects.filter(surname=surname)
            return check_if_queryset_is_empty(owners, 'owners', 'surname',
                                              self.get_serializer, surname,
                                              many=True)
        else:
            return Response({'Test text'})
    """

    # additional action functions.
    @action(detail=False, url_path='search')
    def owners_with_the_given_data(self, request):
        # Try to get parameters from URL request
        name, surname, phone = \
            self.try_to_get_parameters_from_request(request)

        # Owner's parameters search and filter logic with responds.
        #self.owner_parameters_search_logic(name, surname, phone)

        if phone:
            try:
                owner = Owner.objects.get(phone=phone)
                if (not name and not surname or
                name == owner.name and surname == owner.surname or
                name == owner.name and not surname or
                surname == owner.surname and not name
                ):
                    owners = owner
                else:
                    owners = 0
            except Owner.DoesNotExist:
                owners = Owner.objects.filter(phone=phone)


            name_prompt = 'name ' if name else ''
            surname_prompt = 'surname ' if surname else ''
            and_prompt = 'and ' if name or surname else ''

            return check_if_queryset_is_empty(owners, 'owners',
                                              f'{name_prompt}{surname_prompt}'
                                              f'{and_prompt}phone',
                                              self.get_serializer,
                                              *[name, surname, phone],
                                              many=False)

        elif name and surname:
            owners = Owner.objects.filter(name=name, surname=surname)
            return check_if_queryset_is_empty(owners, 'owners',
                                              'name and surname',
                                              self.get_serializer,
                                              *[name, surname], many=True)

        elif name:
            owners = Owner.objects.filter(name=name)
            return check_if_queryset_is_empty(owners, 'owners', 'name',
                                              self.get_serializer, name,
                                              many=True)

        elif surname:
            owners = Owner.objects.filter(surname=surname)
            return check_if_queryset_is_empty(owners, 'owners', 'surname',
                                              self.get_serializer, surname,
                                              many=True)
        else:
            return Response({'You did not put any parameter to search '
                             'function.'})


    @action(detail=False,
            url_path=r'(?P<name_or_surname>[name surname]+)/alphabetic')
    def owners_in_alphabetic_order(self, request, name_or_surname):
        owners = Owner.objects.all().order_by(name_or_surname)
        serializer = self.get_serializer(owners, many=True)
        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('brand', 'model')

    @action(detail=False, url_path='brand')
    def cars_with_the_given_brand(self, request):
        brand = request.GET['brand'].title()
        cars = Car.objects.filter(brand=brand)
        return check_if_queryset_is_empty(cars, 'cars', 'brand', brand,
                                          self.get_serializer, many=True)

    @action(detail=False, url_path='model')
    def cars_with_the_given_model(self, request):
        model = request.GET['model']
        cars = Car.objects.filter(model=model)
        return check_if_queryset_is_empty(cars, 'cars', 'model', model,
                                          self.get_serializer, many=True)

    @action(detail=False,
            url_path=r'(?P<brand_or_model>[brand model]+)/alphabetic')
    def cars_in_alphabetic_order(self, request, brand_or_model):
        cars = Car.objects.all().order_by(brand_or_model)
        serializer = self.get_serializer(cars, many=True)
        return Response(serializer.data)