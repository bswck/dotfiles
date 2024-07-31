alias c=clear
alias pn=pnpm

function where() {
    which -a $1 | uniq
}
