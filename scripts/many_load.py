import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load


from unesco.models import Site, Category, Region, Iso, State



def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    State.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lo = int(row[4])
        except:
            lo = None

        try:
            la = int(row[5])
        except:
            la = None

        try:
            a = int(row[6])
        except:
            a = None

        '''n, created = Site.objects.get_or_create(name=row[0])
        d, created = Site.objects.get_or_create(description=row[1])
        j, created = Site.objects.get_or_create(justification=row[2])
        y, created = Site.objects.get_or_create(year=row[3])
        lo, created = Site.objects.get_or_create(longitude=row[4])
        la, created = Site.objects.get_or_create(latitude=row[5])
        a, created = Site.objects.get_or_create(area_hectares=row[6])'''


        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])



        s = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=lo, latitude=la, area_hectares=a, category=c, state=s, region=r, iso=i)
        s.save()