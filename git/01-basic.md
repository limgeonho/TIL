# git & github

## 분산 관리 시스템

- 변경 된 정보를 업데이트하면서 기록함
- 불필요한 저장공간 낭비 x
- git은 내 사진첩
- github는 원격 드라이브

## git basic

```
$ git init
$ git add .
$ git commit -m 'message'
$ git remote add origin <url>
$ git push origin master
$ git log
$ git status
```



git은 크게 3 가지 단계임

1. add
2. commit
3. push



git bash를 이용해서 github에 업로드하기

1. 내가 원하는 폴더까지 이동(**cd 폴더명**) or 원하는 폴더까지 직접이동 후 **git bash here**실행
2. **git add .** (촬영준비)
3. **git status** 를 통해 commit되었는지 확인(초록 = 이제 commit하면됨, 빨강 = git add . 다시...)
4. **git commit -m "message"** (촬영)
5. **git push origin master** 을 통해 guthub에 업로드
6. 마지막으로 **git log** 를 통해 현재 상태와 push 여부를 확인한다.

