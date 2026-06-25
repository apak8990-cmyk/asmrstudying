(() => {
    const telegram = window.Telegram?.WebApp;

    if (!telegram) {
        return;
    }

    telegram.ready();
    telegram.expand();
    telegram.setHeaderColor("#f4efe8");
    telegram.setBackgroundColor("#f4efe8");
})();
