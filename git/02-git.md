# git(2)

### 1. 지난번 내용에 추가적인 사항

- git bash 에 (master)가 없다면 해당 폴더는 git이 관리하는 파일이 아님

  => 따라서, git init를 명령하고 git이 관리하라는 의미를 부여함.

- 다른 사람이 업로드한 내용을 현재 내 파일에 업데이트 하는 방법

  => git pull origin master

- 다른 사람의 git을 복사하기 위한 방법

  => git clone <https키>

  => <https 키>는 복사해 올 repo의 주소를 적어준다.

2. git 을 github에 올리는  순서
   1. 원하는 폴더에 가서 git bash here
   2. git init(master가 없는 경우만)
   3. git add .
   4. git commit -m "<message>"
   5. git remote add origin <https 주소> => 맨 처음에 한 번만 하면 OK
   6. git push origin master