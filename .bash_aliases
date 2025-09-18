alias c=clear
alias pn=pnpm
alias cp='cp -vi'
alias mv='mv -vi'
alias rm='rm -vi'
alias fd-first='fd --max-results 1'
alias sv='pnpx sv'
alias poetry='uvx poetry'
alias e='exa -F'
alias autin='atuin'
alias pre-commit='prek'

function f() {
    code -r "$1"
}

function sync-fork() {
    git pull upstream main && git push origin main
}

if which wine 1> /dev/null 2>&1; then
    export C=~/.wine/drive_c
    jazz() {
        wine $C/Games/Jazz2/Jazz2.exe $@
    }
fi

function where() {
    which -a $1 | uniq
}

function rm-containers() {
    docker rm -vf $(docker ps -aq)
}

function rm-images() {
    docker rmi -f $(docker images -aq)
}

[[ -f ~/.private_aliases ]] && . ~/.private_aliases
[[ -f .aliases ]] && source .aliases

if [[ -d "$PWD/scripts" ]]; then
    export PATH="$PATH:$PWD/scripts/"
fi

function pymake() {
    # use only in cpython repo!
    if [[ "$OSTYPE" == "cygwin" ]]; then
        PCbuild/build.bat "$@"
    elif [[ "$OSTYPE" == "cygwin" ]]; then
        ./make "$@"
    fi
}
