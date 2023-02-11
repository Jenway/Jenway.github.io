<link rel="stylesheet" class="aplayer-secondary-style-marker" href="\assets\css\APlayer.min.css"><script src="\assets\js\APlayer.min.js" class="aplayer-secondary-script-marker"></script><script type="text/javascript">
      /*  动态标题*/
     var OriginTitile = document.title,
      titleTime;
     document.addEventListener("visibilitychange",
     function() {
      if (document.hidden) {
        document.title = "你别走吖 Σ(っ °Д °;)っ";
        clearTimeout(titleTime)
    } else {
        document.title = "(/≧▽≦/)你又回来啦！" ;
        titleTime = setTimeout(function() {
            document.title = OriginTitile
        },
        2000)
    }
    });
    </script>

<meting-js
    server="netease"
    type="song"
    id="25704085"
    fixed="true">
</meting-js>