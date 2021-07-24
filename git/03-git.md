# git(3)

## 1. 로컬 저장소

- 기존의 디렉토리(폴더) - 아무 기능 없음
- Repository(저장소) - 버전 관리 기능
- git init
  1. 홈폴더에서 git init 절대하지말기
  2. repo안에 또 다른 repo만들지 않기
- repo안에는 
  1. 작업공간(working directory) / 스테이지(staging area) / *저장소(commit)
  2. 분장실 / 촬영장 / *촬영
  3. 코드작성, 수정 / 기록될 파일들의 변경사항들을 스테이지에 올리기 / *스테이지 위의 변경사항들을 저장
- 최초 기본 설정
  1. git config --global user.name <이름>
  2. 서명에 사용할 이름 설정
  3. git config --global user.email <이메일>
  4. 서명에 사용할 이메일 설정
- 작업공간 => git add => 스테이지 => git commit => 저장소
- git log = 저장소에 있는 commit를 확인할 때 사용

## 2. 원격 저장소(remote repo)

- 아이클라우드와 같은 개념
- git에 올린 내용(내 컴퓨터, 로컬)들을 저장할 수 있는 저장소
- 모든 remote저장소는 url이 존재한다(당연한 소리)
- 로컬과 remote를 연결하는 과정
  git remote add <name> <URL>
- 업로드
  git push <name> <branch>
- 원격 저장소는 하나지만 여러 곳에서 접근 가능
- 다른 컴퓨터로 원격저장소에 있는 파일 가져오는 방법
  1. git clone <URL> - 1번 만 하면된다
  2. git pull <name> <branch