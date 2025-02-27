const puppeteer = require("puppeteer");

(async () => {
    console.log("🚀 Launching browser...");
    const browser = await puppeteer.launch({
        headless: false, // False rakho taki UI dikhe
        args: ["--no-sandbox", "--disable-setuid-sandbox"]
    });

    const page = await browser.newPage();
    
    console.log("🌐 Opening Google Colab Fooocus notebook...");
    await page.goto("https://colab.research.google.com/github/lllyasviel/Fooocus/blob/main/fooocus_colab.ipynb#scrollTo=_vkOYRuWLgQi", {
        waitUntil: "networkidle2",
    });

    console.log("🔒 Waiting for Colab to load...");
    await page.waitForTimeout(5000); // Thoda wait karega

    console.log("▶️ Clicking 'Run All'...");
    await page.keyboard.down("Control");
    await page.keyboard.press("F9"); // Ctrl + F9 => Run All
    await page.keyboard.up("Control");

    console.log("⚠️ Checking for 'Run Anyway' warning...");
    await page.waitForTimeout(5000);

    try {
        const runAnywayButton = await page.$x("//button[contains(text(), 'Run anyway')]");
        if (runAnywayButton.length > 0) {
            console.log("✅ Clicking 'Run Anyway'...");
            await runAnywayButton[0].click();
        }
    } catch (error) {
        console.log("❌ 'Run Anyway' button not found, proceeding...");
    }

    console.log("✅ Execution started!");

    // Keep the browser open to keep the session alive
    while (true) {
        await page.waitForTimeout(60000); // Har 1 min me check karega
    }
})();
