const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

async function runTest() {
  // Configure Chrome to suppress unwanted prompts
  let options = new chrome.Options();
  options.addArguments('--no-default-browser-check', '--no-first-run', '--disable-default-apps', '--disable-infobars');

  let driver = await new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

  try {
    // Open the target webpage
    await driver.get('https://pteh.edupage.org/timetable/');

    // Wait for an element to load
    await driver.wait(until.elementLocated(By.id('PRINT_SCENE_BG_1')), 10000);
  } catch (error) {
    console.error('Error during the test:', error);
  } finally {
    // Always close the browser
    await driver.quit();
  }
}

runTest();

// open website, selects class "IPB23" <a> and scope all data in tabel