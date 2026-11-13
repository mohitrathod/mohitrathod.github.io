(function () {
  function initShareButtons() {
    var buttons = document.querySelectorAll('.share-button');

    Array.prototype.forEach.call(buttons, function (button) {
      button.addEventListener('click', function () {
        var url = window.location.href;
        var title = button.getAttribute('data-share-title') || document.title;

        if (navigator.share) {
          navigator.share({ title: title, url: url }).catch(function () {});
          return;
        }

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(function () {
            var original = button.textContent;
            button.textContent = 'Link copied!';
            setTimeout(function () {
              button.textContent = original;
            }, 2000);
          }, function () {
            window.prompt('Copy this link:', url);
          });
          return;
        }

        window.prompt('Copy this link:', url);
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initShareButtons);
  } else {
    initShareButtons();
  }
})();
