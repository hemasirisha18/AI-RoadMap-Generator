(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-42772100-3', 'auto');
ga('send', 'pageview');

$(document).ready(function () {
    $(".js-ht-download-link").click(function() {
        var file = $(this).attr("href");
        console.log("downloading file: " + file);
        ga('send', {
            hitType: 'event',
            eventCategory: 'Download',
            eventAction: file
        });
    });
});
