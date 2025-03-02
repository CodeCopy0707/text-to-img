import { exec } from "child_process";
import fs from "fs";

// Repo URL
const repoUrl = "https://github.com/basujindal/stable-diffusion-cpu.git";
const repoDir = "stable-diffusion-cpu";

// Function to execute shell commands
const runCommand = (command) => {
  return new Promise((resolve, reject) => {
    const process = exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`❌ Error: ${error.message}`);
        reject(error);
        return;
      }
      if (stderr) console.warn(`⚠️ ${stderr}`);
      console.log(`✅ ${stdout}`);
      resolve(stdout);
    });

    process.stdout.pipe(process.stdout);
    process.stderr.pipe(process.stderr);
  });
};

// Deploy Function
const deploy = async () => {
  try {
    // Step 1: Clone Repo if not exists
    if (!fs.existsSync(repoDir)) {
      console.log("🚀 Cloning Stable Diffusion Lite...");
      await runCommand(`git clone ${repoUrl}`);
    } else {
      console.log("✅ Repo already exists. Skipping clone...");
    }

    // Step 2: Install Dependencies
    console.log("📦 Installing dependencies...");
    await runCommand(`cd ${repoDir} && pip install -r requirements.txt`);

    // Step 3: Start Server
    console.log("🔥 Starting Stable Diffusion Lite...");
    await runCommand(`cd ${repoDir} && python app.py --port 8080 --cpu`);

  } catch (error) {
    console.error("❌ Deployment failed:", error);
  }
};

// Run Deploy Function
deploy();
