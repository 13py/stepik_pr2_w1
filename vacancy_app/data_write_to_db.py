import os

from vacancy_app.models import Specialty, Company


def job(works, model_name):
    for work in works:
        model_name.objects.create(title=work.get('title'),
                                  specialty=Specialty.objects.get(code=work.get('cat')),
                                  company=Company.objects.get(name=work.get('company')),
                                  description=work.get('desc'),
                                  salary_min=work.get('salary_from'),
                                  salary_max=work.get('salary_to'),
                                  published_at=work.get('posted')
                                  )


def specialty(specialties, model_name):
    pic_url = 'https://place-hold.it/100x60'
    for spec in specialties:
        code = spec.get('code')
        dir_path = '/home/art/Django/stepik_pr2_patr1/media/specialties'
        way = os.listdir(dir_path)
        for img in way:
            if code in img:
                pic_url = 'specialties/' + img

        model_name.objects.create(code=code,
                                  title=spec.get('title'),
                                  picture=pic_url
                                  )


def company(companies, model_name):
    dir_path = '/home/art/Django/stepik_pr2_patr1/media/logo'
    way = sorted(os.listdir(dir_path))
    pic = iter(way)
    for firma in companies:
        pic_url = 'logo/' + next(pic)
        model_name.objects.create(name=firma.get('title'),
                                  logo=pic_url)
