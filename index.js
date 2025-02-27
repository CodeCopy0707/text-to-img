const puppeteer = require("puppeteer");

(async () => {
    console.log("🚀 Launching browser...");
    const browser = await puppeteer.launch({
        headless: false, // UI visible rahega
        args: ["--no-sandbox", "--disable-setuid-sandbox"]
    });

    const page = await browser.newPage();
    
    console.log("🌐 Opening Google Colab Fooocus notebook...");
    await page.goto("https://colab.research.google.com/github/lllyasviel/Fooocus/blob/main/fooocus_colab.ipynb#scrollTo=_vkOYRuWLgQi", {
        waitUntil: "networkidle2",
    });

    console.log("🔒 Waiting for Colab to load...");
    await page.waitForTimeout(5000); // 5 sec wait

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

    // Wait for the output cell where URLs appear
    await page.waitForTimeout(15000); // 15 sec wait

    console.log("🔍 Searching for Local & Public URLs...");

    const logs = await page.evaluate(() => {
        let outputText = "";
        document.querySelectorAll(".output_text").forEach(el => {
            outputText += el.innerText + "\n";
        });
        return outputText;
    });

    // Extract URLs
    const localhostUrl = logs.match(/http:\/\/127\.0\.0\.1:\d+/)?.[0] || "Not found";
    const publicUrl = logs.match(/https?:\/\/[^\s]+gradio\.live[^\s]*/)?.[0] || "Not found";

    console.log(`\n✅ **Localhost URL:** ${localhostUrl}`);
    console.log(`✅ **Public URL:** ${publicUrl}\n`);

})();
