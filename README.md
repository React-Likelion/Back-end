<div align="center">
<img width="763" alt="image" src="https://user-images.githubusercontent.com/90851865/197409675-2719fbb3-fdee-4bce-b90b-046fb4e3d143.png">
</div>

<br>
<br>


## [SWAGGER Re:act](http://ec2-3-35-49-164.ap-northeast-2.compute.amazonaws.com:8000/swagger/) <br> <br> <img width="1440" alt="스크린샷 2022-10-24 오전 3 29 15" src="https://user-images.githubusercontent.com/90851865/197409373-de2eea4a-30bb-49ff-bab9-9060214bfdda.png">

- 🖥️ UI
|<img width="530" alt="스크린샷 2022-10-24 오전 3 04 53" src="https://user-images.githubusercontent.com/90851865/197408611-008c72a6-cf9c-4d86-a5d5-11807f4ad7cf.png">|<img width="530" alt="스크린샷 2022-10-24 오전 3 04 59" src="https://user-images.githubusercontent.com/90851865/197408623-b54cd82f-92fc-49c0-bae6-b7ea7b555255.png">|<img width="530" alt="스크린샷 2022-10-24 오전 3 05 06" src="https://user-images.githubusercontent.com/90851865/197408637-48b5d5a6-2de9-4230-a466-44072a3ad578.png">|<img width="530" alt="스크린샷 2022-10-24 오전 3 05 15" src="https://user-images.githubusercontent.com/90851865/197408643-ac4de293-0ee7-47e2-8987-ab5e801aaacc.png">|<img width="494" alt="스크린샷 2022-10-24 오전 3 05 28" src="https://user-images.githubusercontent.com/90851865/197408653-e8b633df-4bcf-4f80-8edf-29257fb5a920.png">|
  |:---:|:---:|:---:|:---:|:---:|
  
- 📑 API 설계
    
    **REST API 디자인 가이드 I** <br><br>
    첫 번째, URI는 정보의 자원을 표현해야 한다.  (리소스명은 동사보다는 명사를 사용)<br>
    두 번째, 자원에 대한 행위는 HTTP Method. (GET, POST, PUT, DELETE)로 표현한다.<br>
    
    **REST API 디자인 가이드 II**
    1. 슬래시 구분자(/)는 계층 관계를 나타내는 데 사용
    2. 하이픈(-)은 URI 가독성을 높이는데 사용
    3. 밑줄(_)은 URI에 사용하지 않는다.
    4. URI 경로에는 소문자가 적합하다.
    5. 파일 확장자는 URI에 포함시키지 않는다.
    6. 단수 보다는 복수 사용
    
    [accounts/](https://www.notion.so/146dd55eead14e03b34f12f9ec41c6cf)
    
    [lectures/](https://www.notion.so/7bae3c06f85741dc8c56879015fcf377)
    
    [clubs/ ](https://www.notion.so/77c4539b7c3f4730a3a0f76beefb143c)
    
    [community/](https://www.notion.so/614501115f424d978246f49a6046aa2e)
    
    [mentoring](https://www.notion.so/ca8b77e0ae214e5eb74f17bc14ac3e79)
    
 - 🗄 DB 설계 <br><br>
    <img width="784" alt="스크린샷 2022-10-24 오전 3 03 03" src="https://user-images.githubusercontent.com/90851865/197410471-8b36d1ae-cb31-48f8-bc51-372e82a1ce50.png">

    
    | 1 | 소문자만 사용 |
    | --- | --- |
    | 2 | 테이블 명 snake 지양, 복수형 |
    | 3 | column은 snake 지향, 단수형 |
    | 4 | fk.key → id |
        
    - members
    
        - [User](https://www.notion.so/7a7f526d5d0340d98fbeab9e089d97e3)
        
    - lecture
        - [tags](https://www.notion.so/4038551099694c09b9956d007a4beef3)
            
        - [lectures](https://www.notion.so/9877f4c937d642ed91307bea325c6a8b)
            
    - clubs
        - [clubs](https://www.notion.so/1fa8f57596bc4060affc41ead1498181)
            
        - [clubmembers](https://www.notion.so/d86b93fb14704e8eace9f01e461a637b)
            
        - [clubboard](https://www.notion.so/fd94112a194744359ccbfa15770aac8b)
            
        - [clubboard_comment](https://www.notion.so/181208d664984239bca7cd304a5e21cf)
            
        - [galleries](https://www.notion.so/b9817e87d5bc415ea6440a495ac70679)
            
        - Chatting
            
            firebase 사용
            
    - mentor&mentee
        - [mentorings](https://www.notion.so/8773b022f8e842e0b16354a24ec718ef)
            
        - [mentoring_chat](https://www.notion.so/a8423bc78c374994ab38995b95aa3474)
            
    - community
        - [communityboards](https://www.notion.so/aaec36fe16e04070ab7046a8b4e0582b)
            
        - [communityboardcomments](https://www.notion.so/889a6633b54a4ebdb88d6b4dc56132fd)
    - [jobs](https://www.notion.so/30af1aff1bcc4b76aafa7ec5972cf4c9)
        
    - [locations](https://www.notion.so/dde0d0185f184901a08e4b507db09b97)
        
    - [fields](https://www.notion.so/a493e2c5b81141c5a4e43d17fe8d0728)
