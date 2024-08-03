alias c=clear
alias pn=pnpm

if which wine > /dev/null; then
    export C=~/.wine/drive_c
fi

function where() {
    which -a $1 | uniq
}
