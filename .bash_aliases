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
    cd $2
    code $1 .
    set +x
}

if [ -e ~/.private_aliases ]; then
    . ~/.private_aliases
fi
