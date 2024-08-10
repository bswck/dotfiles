alias c=clear
alias pn=pnpm

if which wine > /dev/null; then
    export C=~/.wine/drive_c
    jazz() {
        wine $C/Games/Jazz2/Jazz2.exe $@
    }
fi

function where() {
    which -a $1 | uniq
}

function pj() {
    set -x
    deactivate 2> /dev/null || :
    cd ${2:-~/Projects}/$1
    code -r .
    set +x
}
