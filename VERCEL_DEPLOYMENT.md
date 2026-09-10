# Deploy the Flask ML App to Vercel

These steps deploy this project as a Vercel Python serverless function.

## 1. Check the required files

The project root must contain:

```text
app.py
requirements.txt
modelD.pkl
scalerD.pkl
templates/
  index.html
  result.html
static/
  style.css
  ...
```

`app.py` loads `modelD.pkl` and `scalerD.pkl` when the application starts. Both files are required at deployment time.

## 2. Install Git and create a GitHub repository

If the project is not already a Git repository, open PowerShell in the project folder:

```powershell
cd "C:\Users\ASUS\OneDrive\Desktop\c\ML_Project"
git init
git add .
git commit -m "Prepare app for Vercel deployment"
```

The repository currently ignores all `.pkl` files. Add the model files explicitly:

```powershell
git add -f modelD.pkl scalerD.pkl
git commit -m "Add trained model artifacts"
```

Create an empty repository on GitHub, then connect and push this project. Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your values:

```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Confirm that `modelD.pkl` and `scalerD.pkl` are visible in the GitHub repository before continuing.

## 3. Add the Vercel configuration

Create a file named `vercel.json` in the project root with exactly this content:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

Commit and push the file:

```powershell
git add vercel.json
git commit -m "Configure Vercel Python runtime"
git push
```

## 4. Deploy from the Vercel dashboard

1. Open [https://vercel.com](https://vercel.com) and sign in with GitHub.
2. Select **Add New...** and then **Project**.
3. Import the GitHub repository containing this project.
4. In **Configure Project**, set **Framework Preset** to **Other**.
5. Set **Root Directory** to `./` unless the project is inside a subfolder.
6. Leave **Build Command** empty.
7. Leave **Output Directory** empty.
8. Do not add a custom **Install Command**. Vercel will install `requirements.txt`.
9. Select **Deploy**.

No environment variables are required by the current application.

## 5. Test the deployment

When the deployment finishes, open the generated Vercel URL. The home page should load at:

```text
https://YOUR_PROJECT.vercel.app/
```

Submit the form with a valid set of values. The form must send these fields, which are read by `app.py`:

```text
Age
BMI
Physical_Activity
Smoked
Gender
HighBP
GeneralHealth
```

A successful submission should open `/predict` and display the prediction result. A direct health check can also be made in PowerShell:

```powershell
Invoke-WebRequest "https://YOUR_PROJECT.vercel.app/" | Select-Object StatusCode
```

The expected status code is `200`.

## 6. View deployment errors

If the deployment fails:

1. Open the project in the Vercel dashboard.
2. Open the failed deployment.
3. Select **Building** to inspect installation/build logs.
4. After a successful build, open **Runtime Logs** and submit the form again.

Common errors:

- `FileNotFoundError: modelD.pkl`: the model file was not pushed, or it is still ignored by Git. Run `git add -f modelD.pkl scalerD.pkl`, commit, and push.
- `ModuleNotFoundError`: add the missing package to `requirements.txt`, then push a new commit.
- Function size or build limit errors: the pinned SciPy/scikit-learn dependencies may be too large for the selected Vercel Python function limits. In that case, deploy the Docker image to a container host instead of Vercel, or reduce the runtime dependencies.
- `405 Method Not Allowed`: the prediction request must be a `POST` request to `/predict`; opening `/predict` directly in a browser is not a valid test.

## 7. Redeploy after changes

After changing Python, HTML, CSS, dependencies, or model files:

```powershell
git add .
git add -f modelD.pkl scalerD.pkl
git commit -m "Update diabetes prediction app"
git push
```

Vercel automatically creates a new deployment for the pushed commit.

## Important notes

- Vercel does not use the included `dockerfile` or `docker-compose.yml` for this deployment.
- The application is serverless on Vercel; it should not depend on a continuously running Flask process.
- Do not store secrets in the repository. Add future secrets under **Project Settings > Environment Variables**.
- The prediction output is a machine-learning estimate and should not be used as a medical diagnosis.
