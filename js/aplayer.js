!(function() {
  var oldLoadAp = window.onload;
  window.onload = function () {
    oldLoadAp && oldLoadAp();

    new APlayer({
      container: document.getElementById('aplayer'),
      fixed: true,
      autoplay: false,
      loop: 'all',
      order: 'random',
      theme: '#b7daff',
      preload: 'auto',
      audio: [
        {
            name: '碧い瞳のエリス',
            artist: '安全地帯',
            url: 'https://doge.ottoli.cn/安全地帯 - 碧い瞳のエリス.mp3',
            cover: 'https://doge.ottoli.cn/aqdd.jpg'
        }
      ]
    });
  }
})();