# airbnb-clone-backend

<details>
<summary> #3.0 Run Server (04:57)
</summary>

**서버 키는 법**

airbnb-clone-backend 폴더 위치 아래에서 터미널을 킨 후 `poetry shell`로 `django` 가상환경으로 들어가준다.
그 다음 `python manage.py runserver` 명령어를 터미널에서 실행해준다.

**서버 닫는 법**

`Ctrl + C`로 중지한다.

</details>

<details>
<summary>
#3.1 Migrations (07:16)
</summary>

**admin page**

/admin/ 페이지로 가려함.

- /admin/ 페이지가 접속이 안되는 경우
  DB에 django_session 이라는 테이블이 없기 때문이다.

서버를 열면서 생긴 'db.sqlite3' 폴더는 DB파일인데 비어있다.

- migration 작업을 통해 문제 해결
  migration은 DB의 state를 수정하는 작업을 의미한다.

  ![Alt text](img/1.png)

  18개의 migration이 있다.

  `python manage.py migrate` 명령어를 터미널에 실행시켜 문제를 해결한다.

  ![Alt text](img/2.png)

- /admin/ 페이지 로그인 시 로그인 오류화면을 볼 수 있음

![Alt text](img/3.png)

</details>

<details>
<summary>
#3.2 Recap (04:57)
</summary>

**migration**

migration 파일에는 DB를 변화시킬 수 있는 python 코드가 들어있다.

이중에는 `auth-user`파일이 있을 것이다. 유저 저장 테이블이다.

</details>

<details>
<summary>
#3.3 Super User (07:24)
</summary>

**관리자 페이지**

터미널을 하나 더 열고 `django` 가상환경으로 들어가준 뒤 `python manage.py createsuperuser`를 실행한다.

비밀번호 설정 시 유효성 검사를 자동으로 해줌을 볼 수 있다.

![Alt text](img/4.png)

`/admin/`으로 들어가 설정한 아이디 비번을 입력하면 관리자 페이지를 볼 수 있다.

![Alt text](img/5.png)

관리자 페이지에서 본인 계정의 비밀번호 변경, 다른 유저의 비밀번호 변경, 유저생성, 그룹생성 등의 작업을 할 수 있다.

</details>

<details>
<summary>
#3.4 Framework vs Library (10:35)
</summary>

**라이브러리와 프레임워크의 차이 설명**

우리가 import를 통해 `라이브러리`를 호출한다.

`프레임워크`는 우리가 쓴 코드를 호출한다.

config폴더의 `setting.py` 파일의 내용을 수정함으로써 사용자의 코드에 맞춰 웹페이지의 내용이 바뀌는 것을 볼 수 있다.

![Alt text](img/6.png)

(프레임워크의 특징이다)

</details>

<details>
<summary>
#3.5 Apps (07:14)
</summary>

**장고의 프로젝트는 application들로 이루어져 있다**

Airbnb를 예시로 든다.

(`room`)숙소 정보와 (`user`)숙소 주인정보나 고객정보를 위한 로직을 같은 파일에 두지 않고 따로 둘 것이다.

`room`을 업로드하고 수정하고 삭제하는 등의 로직과 정보를 DB에 저장하고 변경사항을 적용해야한다.

`user`들이 소통하고 본인의 숙소페이지를 관리하고 본인의 예약정보를 관리하고, DB에 정보를 저장하고 변경사항을 적용해야한다.

</details>

<details>
<summary>
#4.0 Models (10:43)
</summary>

**장고의 프로젝트는 application들로 이루어져 있다**

django가상환경에서 다음 명령어를 터미널에 입력한다.
`python manage.py startapp 어플리케이션_이름`

'어플리케이션\_이름'에 해당하는 폴더가 만들어진다.

house 어플리케이션에 대한 데이터의 detail을 `models.py`에 작성한다.

파일을 수정하고 저장하여도 자동으로 서버가 재시작 되지 않는데 django가 아직 house 어플리케이션에 대해 모르기 때문이다.

config폴더의 `setting.py`파일에 `INSTALLED_APPS`에 우리가 만든 어플리케이션을 추가한다.
![Alt text](img/7.png)

`"houses.apps.HousesConfig"` 추가하기

</details>

<details>
<summary>
#4.1 Migrations (11:55)
</summary>

**Migrations**

django는 자동으로 admin 패널을 우리의 데이터로 생성해준다.

house폴더 아래에 있는 `admin.py`파일에 다음코드를 추가해준다.

```python
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass
```

House라는 모델을 추가해주는 것을 볼 수 있다.

![Alt text](img/8.png)

하지만 눌러보면 table이 없다는 오류가 뜬다.

직접 migration을 함으로써 table을 만들어 줄 수 있다.

새로운 터미널을 열고 django가상환경상태에 진입한 후, `python manage.py makemigrations` 명령어를 입력한다.

![Alt text](img/9.png)

house 폴더 아래에 migration 폴더가 생겼고, 그 안에 '0001_initial.py'파일이 생겼다.

![Alt text](img/10.png)

변경된 데이터베이스를 적용하기 위해 `python manage.py migrate` 명령어를 입력해준다.

![Alt text](img/11.png)

그러면 이제 Houses를 눌렀을 때 migrate한 데이터베이스가 보인다.

![Alt text](img/12.png)

'ADD HOUSE' 버튼을 눌러 예전에 미리 설정해두었던 db자료형에 맞춰 내용을 추가할 수 있다.

![Alt text](img/13.png)

Houses에 내용물을 하나 추가하고 서버를 껐다키면 전에 추가했었던 내용이 살아있는 것을 확인할 수 있다.

![Alt text](img/14.png)

</details>

<details>
<summary>#4.2 Recap (10:49)</summary>

기존에 설치된 앱과 새로만들어 추가한 앱을 분리하여 따로 합쳐준다.

`INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS`

migration을 테스트해보기위해 house폴더 아래에 있는 `models.py`에서 'price'를 'price_per_night'로 바꾼 후 변경사항을 적용시키기 위해 migration을 해준다.

![Alt text](img/15.png)

migration폴더 아래에 새로운 파이썬 파일이 생기고 변경사항이 기록된다.

![Alt text](img/16.png)

변경사항을 `python manage.py makemigrations`로 등록해주고, `python manage.py migrate`로 적용해준다.

![Alt text](img/17.png)

적용된 모습이다.

</details>

<details>
<summary>#4.3 Admin (13:08)</summary>

**admin 패널 추가설정하기**

admin패널에 들어가면 Houses 클래스로부터 만들어진 항목의 이름이 'House object(1)' 로 보인다.

model.py에서 House클래스에 `__str__()` 메소드를 수정해줌으로써 우리가 원하는 형태로 보이게 할 수 있다.

```
    def __str__(self):
        return self.name
```

admin.py에서 `list_display=[]`에 데이터 속성이름을 적어주면 해당 속성들을 미리보기 가능하다.

```
    list_display = [
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    ]
```

`list_filter=[]`를 추가해주면 오른쪽에 필터목록을 볼 수 있다.

![Alt text](img/18.png)

```
    list_filter = [
        "price_per_night",
        "pets_allowed",
    ]
```

`    search_fields = ["address"]`이 코드를 추가 함으로써 주소를 기준으로 검색할 수 있는 검색창이 생긴다.

`"address_startwith"`를 집어넣으면 검색키워드로 시작하는 것만 뜨고, 그냥 `"address"`만 넣으면 키워드가 중간에 들어있어도 모두 검색된다.

</details>

<details>
<summary>#4.4 Documentation (13:33)</summary>

**Documentation**

[장고문서](https://docs.djangoproject.com/en/4.2/ref/models/fields/)

Documents를 통해 admin패널에서 도움말, 데이터 이름, 데이터 숨기기, 리스트상태에서 수정가능하게 하기 등등의 많은 기능을 적은 코드로 사용할 수 있다.

It's insane~

</details>

<details>
<summary>#5.0 Introduction (11:52)</summary>

**User Applications 환경설정\_0**

인터프리트 설정을 poetry환경으로 잡아준다.

그러면 django 임포트할때 밑에 경고물결줄이 안뜬다.

</details>

<details>
<summary>#5.1 Custom Model (13:53)</summary>

**User Applications 환경설정\_1**

[Documents Link](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model)

`python manage.py startapp users`로 새로운 커스텀 유저를 만들어준다.

기존 유저의 모든 것을 상속받아야함.

1.  `AbstractUser`의 모든 것을 상속받은 `User`를 커스터마이징하고,

2.  커스터마이징한 `User`를 Django에게 사용하겠다고 인지시켜야한다.

    2-1. 링크에서 추가해야하는 코드를 `setting.py`에 추가한다.

    2-2. user application을 설치해야하므로 `CUSTOM_APPS`에 추가해준다.

    2-3. 커스텀 USER를 만들었는데 이미 옛날에 만들어둔 USER와 충돌을 일으키기 때문에 서버를 끄고 DB를 삭제해준다. "db.sqlite3"을 삭제한다. 서버 재실행해준다.

    2-4. 그리고 houses에 있는 migrations 파일도 지워준다.(0001\_.... 이렇게 생긴 파일들). (폴더와 `__init__.py` 파일은 살려둠)

    2-5. `python manage.py makemigrations`를 해준다.

    ![Alt text](img/19.png)

    2-6. `python manage.py migrate`로 새정보로 업데이트해주고, 동기화된다.

3.  user모델을 admin패널에 추가한다.

    3.1 users폴더에 admin.py에 내용을 추가해준다.

    3.2 다시 페이지를 리로드하면 로그인을 다시해야하는데, DB를 지웠기 때문에 세션이 종료된 것이고, user로 새로 생성해 줘야한다.

    따라서 `python manage.py createsuperuser`로 user계정을 새로 만들어준다.

![Alt text](img/20.png)

유저가 분리되어 보인다. 이전에는 Groups와 같이 있었다.

</details>

<details>
<summary>#5.2 Custom Fields (06:23)</summary>

**Custom User Model**

파이썬 코드에 있는 모델 구조와 DB구조를 서로 동기화 하기 위해 추가작업(기본값 넣어주기 등의 작업)을 해줘야 한다.

만약 'is_host'필드에 기본값을 지정해주지 않고 `python manage.py makemigrations`를 해주면 동기화를 위한 오류를 발생시킬 것이다.

![Alt text](img/21.png)

추가한 'is_host' 필드는 기본값없이 Nill 값으로 추가가 불가능하다는 오류이다.

옵션1. 일회성 기본값제공하기. 하지만 기존 행들의 이 열 값들이 모두 null값이 된다.

옵션2. 이 작업을 중지하고 models.py에서 기본값을 지정해준다.

2번을 선택하여 추가작업을 해줄 것이다.

</details>

<details>
<summary>#5.3 Defaults (11:04)</summary>

**Adding Default**

DB를 수정하여 기존에 있었던 필드가 사라지면 원래 있어야 할 것이 없어져서 오류가 발생한다.

default 값이 필요한 필드에 default값을 넣어주고 makemigrations를 해준다.

웹에서 유저를 클릭하여 들어가보자.

하지만 필드가 non-editable 상태여서 오류가 발생하는 것을 볼 수 있다.

다음 강의에서 해결한다.

</details>

<details>
<summary>#5.4 Custom Admin (08:34)</summary>

**Admin pages modify**

어드민 페이지를 수정하였다.

</details>
<details>
<summary>#5.5 Foreign Keys (13:16)</summary>

**유저 연동시키기(model연결시키기)**

ForeignKey를 사용하여 사용자를 연결한다.

만약 사용자가 지워지면 어떻게 처리할 것인지 정해주어야만 한다.

NULL로 처리해줄 수 있다. 하지만 그 유저가 만든 house가 주인이 없는 채로 남아있으면 안됨으로 house도 같이 delete해주기 위한 CASCADE를 쓴다. `on_delete=models.CASCADE`

그 다음 db.sqlite3과 migrations 폴더에 있는 파일들을 모두 지워준다.(`__init__.py` 빼고)

초기화 해주는 과정이다.

초기화가 되었기 때문에 makemigrations, migrate, createsuperuser를 다 해준다.(jeongyeon, 123)

웹페이지에 들어가서 house에 추가를 해주면 아래에 새로운 필드가 생긴 것을 확인할 수 있다.

![Alt text](img/23.png)

박스를 클릭하면 사용자를 선택해줄 수 있다. 초기여서 '-----'와 'jeongyeon' 2개만 있다.

house가 user의 ForeignKey를 가지고 있다고 알려주었기 때문에 models를 연결할 수 있었다.

PositiveIntegerField를 사용하게되면 단순히 숫자를 저장하기만 한다. 하지만 ForeignKey를 사용하면 Django에게 참조하고 싶은 model을 알려줌으로써 연결을 해준다.

</details>

<details>
<summary>#5.6 Super Mega Recap (16:07)</summary>

**관계형DB를 Django에서 다루기**

사용자를 예시로 user테이블과 house테이블을 연결하였다.

만약 user테이블에있는 user가 하나 사라진다면, 그 user와 연관된 house를 어떻게 처리할 것인지가 문제가 된다.

house를 같이 삭제시키는 방법과 house의 user정보를 null로 만들어버리는 방법 2가지가 있다.

extensions에서 sqlite viewer를 설치하면 django의 sqlite db를 시각화해서 볼 수 있다.

다음에 model들을 생성할 것이기 때문에 house폴더를 삭제시켰다. 그리고 setting.py에서 custom_apps에 있는 house도 지워준다.

그다음 migration폴더에 있는 것도 지워서 초기화 해준다.

</details>
<details>
<summary>#6.0 User Model (11:38)</summary>

**최종 프로젝트에서 사용할 model만들기**

user 모델을 확장하였음

</details>
<details>
<summary>#6.1 Room Model (07:08)</summary>

**최종 프로젝트에서 사용할 model만들기**

rooms 모델을 새로 만들어줌

콘솔창에 `python manage.py startapp rooms`를 쳐서 새 모델을 만들어 주고, Config폴더에 있는 settings.py에 CUTSTOM_APPS에 `"rooms.apps.RoomsConfig",` 을 추가한다.

many-to-many 것들을 위해 나머지는 다음강의에

</details>
<details>
<summary>#6.2 Many to Many (13:19)</summary>

**최종 프로젝트에서 사용할 model만들기**

many to many 의 의미를 알기 위해서는 Many to one, One to many의 의미를 알아야 한다.

- room1, room2, room3 -> user1 (Many to one)

- user1 -> room1, room2, room3 (One to many)

Amenty model이 many to many relationship을 가진다.

Amenity1, Amenity2, Amenity3 => room1, room2, room3

그리고 반복을 피하기 위해서 생성된 날짜, 변경수정된 날짜를 저장하는 필드를 하나 만들어준다.

여기서 `auto_now_add=True`를 해주게 되는데 처음 생성되었을 때 날짜를 넣어주는 기능이다.

update는 `auto_now=True`를 넣어줘서 저장될 때마다 시간이 기록되게 한다.

근데 여기서 만들고 있는 시간 저장기능은 다른곳에서도 똑같이 사용될 것이다. 그러면 반복적으로 같은 코드를 사용해줘야하는데 이 중복되는 것을 막기 위해서 새로운 application을 만들어줄 것이다.

콘솔에 `python manage.py startapp common`으로 공통 코드를 위한 새 application을 만들어준다.

이 새로 만들어준 common모델에는 추상모델을 만들어준다. 이 모델은 db에 추가하지 않고 다른 모델에서 재사용하기 위한 모델이다. 이것은 blueprint같은 모델이다.

만들어준 common 모델에 아래부분에

```(python)
class Meta:
    abstract = True
```

을 적어준다면 django는 이 모델에 대해서 쓸모없는 db를 만들어내지 않는다.

사용하기 위해서는 사용하고자 하는 모델에 임포트를 먼저 한 후 `from common.models import CommonModel` 시작할 때 modles.Model부분을 `CommonModel` 로 바꿔적어주면 된다.

</details>
<details>
<summary>#6.3 Recap (08:00)</summary>

**최종 프로젝트에서 사용할 model만들기**

만든 rooms와 amenities를 웹상에서 확인해봄.

db에서 직접 확인해보면 생성날짜 수정날짜도 확인할 수 있다.

</details>
<details>
<summary>#6.4 Rooms Admin (12:49)</summary>

**최종 프로젝트에서 사용할 model만들기**

room과 amenity의 이름 수정

그리고 Amenity모델을 자동으로 복수형으로 표시하는 django의 기능 중 Amenitys라고 잘못된 복수형을 다음 코드로 바로잡아준다.

```(python)
class Meta:
    verbose_name_plural = "Amenities"
```

admin.py에서 목록에서 어떻게 보일지, 어떤 필터 적용기준으로 보여줄지 패널에서 시각화 할 수 있다.

</details>
<details>
<summary>#6.5 Experiences (12:27)</summary>

**최종 프로젝트에서 사용할 model만들기**
experience창 만들기

</details>

<details>
<summary>#6.6 Categories (11:02)</summary>

**최종 프로젝트에서 사용할 model만들기**
category 연결 만들기

</details>
<details>
<summary>#6.7 Reviews (08:28)</summary>

**최종 프로젝트에서 사용할 model만들기**
review 테이블만들기

</details>
<details>
<summary>#6.8 Wishlists (05:45)</summary>

**최종 프로젝트에서 사용할 model만들기**
wishlist 만들기

</details>

<details>
<summary>#6.9 Bookings (14:42)</summary>

**최종 프로젝트에서 사용할 model만들기**
booking 만들기

-> rooms, experiences 2개 모두 예약할 수 있는 booking기능을 만들 것이다. 2개중 선택을 할 수 있도록 choice클래스를 하나 만들어준다.

booking에서 check_in, check_out을 만들어 줄 때에는 DB에 시간을 포함하여 저장할 것인지 날짜만 저장할 것인지를 우리가 정하여 만들어줘야 한다.(여기서는 날짜만 저장하기로 함)

</details>
<details>
<summary>#6.10 Medias (10:11)</summary>

**최종 프로젝트에서 사용할 model만들기**
Media 만들기

OneToOneField를 만들었는데 고유한 것을 연결할 때 사용하였다.(드물게 사용함)

</details>

<details>
<summary>#6.11 Direct Messages (15:21)</summary>

**최종 프로젝트에서 사용할 model만들기**
direct_messages 만들기

dms로 이름지어도 되어서 그렇게 했음

application이름은 해당 모델의 폴더 아래에 app.py에서 name을 수정함으로서 바꿀 수 있다.

admin패널에서 추가적으로 문자 개수, 채팅방에 참여하고있는 사람수, 개시한 방에 평점 등의 추가적인 속성을 넣어줄 수 있을 것이다.

</details>
<details>
<summary>#7.0 Introduction (10:58)</summary>

**Django의 ORM**

콘솔창에서 shell로 db와 소통할 것이다.

`python manage.py shell`

models를 통해 db에 접근한다.

db에 있는 모든 room찾기

`from rooms.models import room`

`Room.objects.all()`

어떠한 속성으로도 찾을 수 있다.

`Room.objects.get(name="서울집")`

.get 뿐만아니라 .create, .filter도 있다

`room = Room.objects.get(name="서울집")`

처럼 변수에 저장하고

`room.created_at`,`room.name`,`room.id`등의 명령어를 입력할 수 있다.

`room.price = 2000`으로 하고 `room.save()`를 하게되면 db가 업데이트된다. 심지어 updated_at에 시간이 반영된다. 하지만 국제표준시간 기준이여서 9시간 느리게 보인다.

</details>

<details>
<summary>#7.1 filter, get, create, delete (14:10)</summary>

**ORM 용어들**

- `.get()` 특정한 object 하나만 찾고 싶을때

  `Room.objects.get(pk=1)` primary key 1로 찾을때

- `.filter()` 필터적용하여 가져오기

  - `Room.objects.filter(pet_friendly=True)`
    'pet_friendly'를 필터적용하여 가져오면 결과값 개수가 1개 이상이므로(0개가 나올 수 있음) `.filter()`를 사용해야한다. 만약 `.get()`을 사용하면 오류가 날 것이다.

  - filter는 유용하다. '속성'+ '\_\_필터값' 형식으로 underscore를 이용한다.

  - 부등호도 사용하다.

  `Room.objects.filter(price__gt=15)`

  - 검색어도 사용가능하다('seoul'이 들어간 방만 찾기 같은 행위)

    `Room.objects.filter(name__contains="서울")`

    `Room.objects.filter(name__startswith="서울")`

- `.all()` 모든것을 보여줌

- `.create()` db내용물 생성하기

  괄호안에 속성값을 잘 넣어줘야한다.

  `Amenity.objects.create(name="Amenity from the Console",  description="cool")`

- `.delete()` 선택한 db값을 삭제할 수 있다.

  `.get()`으로 삭제하고싶은 것을 고르고 삭제해준다.
  `Amenity.objects.get(pk=4).delete()`

      </details>

  <details>
  <summary>#7.2 QuerySets (07:01)</summary>

**QuerySets은 무엇인가**

연산자를 함께 묶어주는 역할을 한다.

filter 사용시 여러 속성을 ','로 묶어줄 수 있다.

db와 소통하지 않고 db에 있는 모든 데이터를 몽땅 꺼내온다.

QuerySet은 구체적으로 요청받을 때만 데이터를 제공할 것이다.

명령을 즉시 실행시켜주지 않고 데이터를 요청할 때만 제공한다.

1. 게으르기 때문에 db를 힘들게 하지 않는다.

2. 서로다른 QuerySet들을 연결할 수 있다.

all같은 db를 힘들게 할 수 있는 명령어를 실행한다면 db를 바로 다 보여주지 않고 QuerySet형태로 짧게 보여준다.

</details>

<details>
<summary>#7.3 Admin Methods (14:34)</summary>

**lookup 무엇인가**

"\_\_"연산자는 lookup연산자라고 부른다.

[Documentation link](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups)

QuerySet을 반환하는 메소드도 있고, 반환하지 않는 메소드도 있다.

새로운 db 콘솔 지식을 통하여 admin 패널에서 더 많은 것을 할 수 있다.

예를들면 .count()메소드를 통해 얼마나 많은 요소들이 있는지를 표시해줄 수 있다.

`"total_amenities",`이 항목을 rooms의 admin.py에 추가할 것이다. 하지만 이것은 미리 만들어주지 않았기 때문에 오류가 발생한다.(Room클래스의 메소드로 찾아내려 한다.)

2가지 방법이 있다.

1. 직접 model에 메소드를 추가하기. ORM을 이용하는 방법이다.

2. admin.py에 직접 메소드를 만들어주기. 메소드는 self뿐만 아니라 room도 매개변수로 갖게된다.

1번방법은 room에 항상 total_amenities메소드가 따라다닐 것이다. room을 쓸때마다 total_amenities도 필요하다면 1번방법이 좋다. 2번방법은 관리자 패널에서만 확인할 수 있다. 다른곳에서는 전혀 필요없고, 관리자 패널에만 필요하다면 2번방법이 좋을 수 있다.

```
#(admin.py)
def total_amenities(self, room):
    return room.amenities.count()
```

```
def total_amenities(self):
    return self.amenities.count()
```

이렇게 해줌으로서 count()메소드로 amenities개수를 표현해줄 수 있다.

</details>
<details>
<summary>#7.4 ForeignKey Filter (11:33)</summary>

**foreignKey로 필터링하기**

reverse accessors : 관계를 뒤집어서 접근하도록 하는 것.

사용하는 이용 : 반대방향으로 원하는 정보를 찾을 때

room 모델은 user모델을 foreignKey로 포인팅하고 있다.

reverse란 user를 가리키고 있는 model을 찾기 위한 것. 반대방향으로 원하는 것을 찾아가는 것.

예를 들어 room.owner은 room에서 user를 찾아내는 것이다. 근데 user에서 room을 찾아내는 방법, 이것이 reverse이다.

`Room.objects.filter(owner__username="jeongyeon")`

이런식으로 작성하면 해당 유저의 모든 room을 QuerySet으로 보여준다.

`Room.objects.filter(owner__username__startswith="j")`

이런것도 가능하다(~로 시작하는 것 찾기 필터)

이런 기능이 반복적으로 많이 필요한 경우가 있다. 예를들어 인스타그램에서 creater가 사진을 올리는 기능이 있고 그 creater를 클릭하여 그사람이 올린 사진들을 보는 행위 reverse가 있는데 둘다 반복적으로 많이 쓰이는 기능이 될 것이다.

room.owner.username은 가능하다. 방을 업로드한 유저의 이름을 보는 기능이다. 하지만 반대로 유저의 이름을 기준으로 그 유저가 올린 방을 모두 찾아보는 기능 user.rooms 이러한 기능은 만든적이 없다. reverse로 찾아야 하는 것이다. 하지만 코드를 손봐서 기능을 만들어 줄 수 있다.

</details>
<details>
<summary>#7.5 Reverse Accessors (11:27)</summary>

**Reverse Accessors**

콘솔에서 User를 임포트해와서 pk=1을 me라는 변수에 저장하자.

`dir(me)`를 통해 많은 메소드와 속성을 볼 수 있다.

`~_set`이라는 것이 많다. 이것이 reverse accessors이다.

`me.room_set.all()`을 입력하면 해당 유저의 모든 room을 보여준다.

새로운 유저를 만들어주자. (admin, adminpw1234) 방하나를 admin의 방으로 바꿔준다.

다시 명령어를 입력하면 방이 하나 없어져있다.

규칙 : ForeignKey는 매번 `_set`속성을 받는다.

review에서도 user와 연결시 ForeignKey를 사용했다. 따라서 `me.review_set`이 가능하다.

</details>
