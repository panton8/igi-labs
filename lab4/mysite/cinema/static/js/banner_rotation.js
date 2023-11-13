  // Настройки ротации баннеров
  var rotationIntervalElement = document.getElementById("rotationInterval");
  var rotationInterval = rotationIntervalElement.getAttribute("data-rotation-interval");
  var rotateBanners = true; // По умолчанию ротация включена


  // Функция для смены баннеров
  function changeBanner() {
    var slides = document.querySelectorAll('.slide');
    var currentBanner = 0;

    return function () {
      slides[currentBanner].style.display = 'none';
      currentBanner = (currentBanner + 1) % slides.length;
      slides[currentBanner].style.display = 'block';
    };
  }

  var rotate = changeBanner();

  // Функция для включения/выключения ротации
  function toggleRotation() {
    if (rotateBanners) {
      clearInterval(rotationIntervalId);
    } else {
      rotationIntervalId = setInterval(rotate, rotationInterval);
    }
    rotateBanners = !rotateBanners;
  }

  // Обработчик фокуса страницы
  window.addEventListener('focus', function () {
    if (rotateBanners) {
      rotationIntervalId = setInterval(rotate, rotationInterval);
    }
  });

  window.addEventListener('blur', function () {
    clearInterval(rotationIntervalId);
  });

  // Начинаем ротацию (если включена)
  var rotationIntervalId = null;
  if (rotateBanners) {
    rotationIntervalId = setInterval(rotate, rotationInterval);
  }
