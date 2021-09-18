# git branch

- 협업의 핵심
- https://backlog.com/git-tutorial/kr/ 참고

- 통합브랜치(master)

  - 언제든지 배포할 수 있는 버전을 만들 수 있어야 하는 브랜치

- 토픽브랜치(ex: b1, b2, b3...)

  - 기능별로 나눠서 작업하는 브랜치
  - 기능완료나 작업완료 후에는 통합브랜치를 합쳐(merge)주어야한다

- git은 무조건 commit단위로 생각하자!!!

  -> commit을 안하면 git이 관리 하지 않음

- branch

  - 새로운 branch만드는 방법

    -> git branch b1

  - 새롭게 만든 branch로 변경하는 방법

    -> git switch b1

  - 새롭게 branch만들고 바로 switch하는 방법

    -> git switch -c b2

- branch와 master

  - branch에서 작업한 내용은 commit해야한다 -> 그래야 git이 관리함	
  - 하지만 switch master하면 branch에서 작업한 내용이 보이지 않는다.
  - 왜?
  - merge 하지 않았기 때문에 master에 반영되지 않는다
  - HEAD를 master로 옮긴 후에 git merge branch한다
  - master에서 branch를 확인할 수 있음
    - git log --oneline 를 통해서 현재까지 commit을 확인할 수 있음
    - git log --oneline --graph하면 그림으로 나옴

- (master)에서 git merge branch했을 경우에 만약에 conflict가 난다면?

  - 원하는 방향으로 직접 conflict를 수정해서 add . -> commit -> 다시 merge하면된다.

- remote에 있는 master에서 현재 가장 안정된 상태를 가져오기 위해서는

  -> git pull origin master하면 된다.

- ```bash
  ~/git_branch
  $ touch README.md .gitignore
  
  ~/git_branch
  $ git init
  
  ~/git_branch (master)
  $ git add .
  
  ~/git_branch (master)
  $ git commit -m 'first commit'
  [master (root-commit) 5a14295] first commit
   2 files changed, 188 insertions(+)        
   create mode 100644 .gitignore
   create mode 100644 README.md
  
  ~/git_branch (master)
  $ git add README.md
  
  ~/git_branch (master)
  $ git commit -m '2'
  [master 34195be] 2
   1 file changed, 6 insertions(+), 1 deletion(-)
  
  ~/git_branch (master)
  $ git log --oneline
  34195be (HEAD -> master) 2
  5a14295 first commit
  
  ~/git_branch (master)
  $ git branch b1
  
  ~/git_branch (master)
  $ git log --oneline
  34195be (HEAD -> master, b1) 2
  5a14295 first commit
  
  ~/git_branch (master)
  $ git switch b1
  Switched to branch 'b1'
  
  ~/git_branch (b1)
  $ git switch master
  Switched to branch 'master'
  
  ~/git_branch (master)
  $ git add .
  
  ~/git_branch (master)
  $ git commit -m '3'
  On branch master
  nothing to commit, working tree clean
  
  ~/git_branch (b1)
  $ git log --oneline
  eb9abb1 (HEAD -> b1) 3
  34195be (master) 2
  5a14295 first commit
  
  ~/git_branch (b1)
  $ git switch master
  Switched to branch 'master'
  
  ~/git_branch (master)
  $ git switch b1
  Switched to branch 'b1'
  
  ~/git_branch (b1)
  $ touch secret.txt
  
  ~/git_branch (b1)
  $ git status
  On branch b1
  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          secret.txt
  
  nothing added to commit but untracked files present (use "git add" to track)
  
  ~/git_branch (b1)
  $ git commit -m '4'
  [b1 6613801] 4
   1 file changed, 0 insertions(+), 0 deletions(-)
   create mode 100644 secret.txt
  
  ~/git_branch (b1)
  $ git switch master
  Switched to branch 'master'
  
  ~/git_branch (master)
  $ git merge b1
  Updating 34195be..6613801
  Fast-forward
   README.md  | 3 ++-
   secret.txt | 0
   2 files changed, 2 insertions(+), 1 deletion(-)
   create mode 100644 secret.txt
  
  ~/git_branch (master)
  $ git log --oneline
  6613801 (HEAD -> master, b1) 4
  eb9abb1 3
  34195be 2
  5a14295 first commit
  
  ~/git_branch (master)
  $ git branch b2
  
  ~/git_branch (master)
  $ git log --oneline
  6613801 (HEAD -> master, b2, b1) 4
  eb9abb1 3
  34195be 2
  5a14295 first commit
  
  ~/git_branch (master)
  $ git branch
    b1
    b2
  * master
  ```

- 그렇다면 실제로 다른 사람들과 협업할때는?

  - 위와 같은 방법으로 무작정 master에 merge하면 절대 안된다!!!!!!!!!!!

  - 따라서, master에서 먼저 내가 작업할 공간으로 pull해온다

    -> git pull origin master

  - 다음으로 작업을 실시한다.

  - 작업을 마친 다음에는 master에 직접이 아닌 

    -> git push origin dev-a

    -> dev-a가 작업한 내용으로 origin(remote)에 push 한다

  - 그 다음에 관리자에게 dev-a가 작업한 내용을 master에 merge해도 되는지 여부를 허락받는다

    -> merger request과정

  - 허락 받으면 merge된다

  - ![1](https://user-images.githubusercontent.com/73927750/133880632-7b58128e-44e9-424a-a032-9aa9fcaafb43.JPG)

  - ![2](https://user-images.githubusercontent.com/73927750/133880644-3b892236-209e-4636-95e6-81446dc00278.JPG)

