call plug#begin('~/.vim/plugged')
Plug 'chriskempson/base16-vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'L04DB4L4NC3R/texgroff.vim'
call plug#end()

let base16colorspace=256

let &t_ZH = "\e[3m"
let &t_ZR = "\e[23m"

let &t_SI = "\<esc>[5 q"
let &t_SR = "\<esc>[5 q"
let &t_EI = "\<esc>[2 q"

colorscheme base16-default-dark

" set number

function! s:base16_customize() abort
  call Base16hi("MatchParen", g:base16_gui05, g:base16_gui03, g:base16_cterm05, g:base16_cterm03, "bold,italic", "")
endfunction

augroup on_change_colorscheme
  autocmd!
  autocmd ColorScheme * call s:base16_customize()
augroup END

if filereadable(expand("~/.vimrc_background"))
  let base16colorspace=256
  source ~/.vimrc_background
endif
