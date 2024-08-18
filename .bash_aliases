alias c=clear
alias pn=pnpm

if which wine 1> /dev/null 2>&1; then
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
    cd $2
    code $1 .
    set +x
}

[ -e ~/.private_aliases ] && . ~/.private_aliases
