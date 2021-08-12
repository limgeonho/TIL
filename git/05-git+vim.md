# git(5) + vim

## 1. Vim

- cui 용 텍스트 편집기
- 사용방법
  - 일반모드 => i => 입력가능(입력모드) => esc => 일반모드(돌아오기)
  - 일반모드 => : => 명령모드
  - 명령모드 => : + (w, q, (qw, x), q!) => (저장, 종료, (저장+종료), 강제종료)
- git commit --amend : 직전에 쓴 commit message 수정

## 2. git branch

- branch == 포인터

   => 난 지금 현재 이러한 commit를 가리키고 있는거임

- HEAD `<name>` 

  => 현재 작업하고 있는 포인터의 이름

- git branch `<name>`

  => 새로운 branch생성

- git push origin master:`<name>`

  => name이름으로 push하겠다