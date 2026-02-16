const { Builder } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

(async () => {
  const options = new chrome.Options();
  options.addArguments('--headless=new');

  const driver = await new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

  await driver.get('https://pteh.edupage.org/timetable/');

  await driver.sendDevToolsCommand('Network.enable');

  driver.on('Network.responseReceived', async (params) => {
    if (params.response.url.includes('getTTViewerData')) {
      const body = await driver.sendDevToolsCommand(
        'Network.getResponseBody',
        { requestId: params.requestId }
      );
      console.log("Timetable JSON:", body.body);
    }
  });

  await driver.sleep(6000);
  await driver.quit();
})();
