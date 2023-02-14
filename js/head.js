document.addEventListener('visibilitychange',function(){
    if( document.visibilityState == 'hidden' ){
        normal_title = document.title;
        document.title = '哎你别走吖 Σ(っ °Д °;)っ';
    }else{
        document.title = '(/≧▽≦/)咦！你又回来啦';
        setTimeout(function(){
            document.title = normal_title;
        }, 1200)
    }
});