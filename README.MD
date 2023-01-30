

# Installing Bazel on macOS

### Step 1: Install Homebrew on macOS

Install [Homebrew](https://brew.sh/) (a one-time step):

```posix-terminal
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```


### Step 2: Install Bazel via Homebrew

Install the Bazel package via Homebrew as follows:

```posix-terminal
brew install bazel
```


# Installing Bazel on Ubuntu


### Step 1: Add Bazel distribution URI as a package source

## Using Bazel's apt repository

**Note:** This is a one-time setup step.

```posix-terminal
sudo apt install apt-transport-https curl gnupg -y
curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor >bazel-archive-keyring.gpg
sudo mv bazel-archive-keyring.gpg /usr/share/keyrings
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/bazel-archive-keyring.gpg] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
```

The component name "jdk1.8" is kept only for legacy reasons and doesn't relate
to supported or included JDK versions. Bazel releases are Java-version agnostic.
Changing the "jdk1.8" component name would break existing users of the repo.

### Step 2: Install and update Bazel

```posix-terminal
sudo apt update && sudo apt install bazel
```
