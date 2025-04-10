augroup JavaClassTemplate
  autocmd!
  autocmd BufNewFile *.java call JavaClassTemplate()
augroup END

let s:pluginHome = expand("<sfile>:p:h:h")
let s:loadScript = 1

function! JavaClassTemplate() 
	if has('python3')
		if s:loadScript
			execute "py3file " . substitute(s:pluginHome, "\\", "/", "g") . "/pythonx/jct.py"
			
			let s:loadScript = 0
		endif

		execute "python3 jct_template()"
	else
		echom 'JavaClassTemplate: No python support'
	endif
endfunction
