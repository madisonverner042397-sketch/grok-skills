---
name: github-mobile
description: Help someone install, sign in to, and use GitHub Mobile on Android or iOS, including multiple accounts, social login, GHE.com and GitHub Enterprise Server prerequisites, language settings, iOS Universal Links, and leaving the TestFlight preview. Use when the user asks how to do something in the GitHub Mobile app, can't sign in or get notifications on mobile, wants to add or switch accounts, or wants GitHub links to open in Safari instead of the app.
license: CC-BY-4.0
metadata:
  source: https://docs.github.com/en/get-started/using-github/github-mobile
  tags:
    - github
    - mobile
    - ios
    - android
    - notifications
---

# GitHub Mobile

Answer questions about the GitHub Mobile app for Android and iOS. Give the exact taps, check prerequisites before troubleshooting, and send the user to the official docs for anything this playbook doesn't cover.

## When to Use

- "How do I add my work account to GitHub Mobile?"
- "GitHub Mobile won't connect to our Enterprise Server"
- "Can I sign in with Google or Apple?"
- "GitHub links keep opening in the app, I want Safari"
- "How do I leave the GitHub iOS beta?"
- The user wants to know what they can and can't do from the mobile app

## Inputs and Access

- From the user: the platform (Android or iOS), the account type (GitHub.com, GHE.com, or GitHub Enterprise Server), and, for sign-in or feature problems, the app version (in the app's **Settings**) and, for Enterprise Server, the server version if they know it.
- No logins, app access, or permissions are needed: this playbook only gives instructions. If a detail is missing and changes the answer, ask for it; otherwise answer for the common case and say which case you assumed.

## Workflow

1. **Identify the platform and account type.** Ask, or infer from context:
   - Android or iOS
   - GitHub.com, GHE.com (data residency, `SUBDOMAIN.ghe.com`), or GitHub Enterprise Server
2. **Check prerequisites first** (see below). Most sign-in failures come from an app version that's too old, a server that's too old, or mobile support turned off by the admin.
3. **Give step-by-step instructions** using the exact UI labels in bold (for example, **Profile**, **Manage Accounts**).
4. **State limits plainly.** If a feature isn't on mobile, or depends on the enterprise, say so instead of guessing at a workaround.
5. **Link the matching official docs page** when the topic goes deeper (notifications, 2FA, code search, Copilot).

## Output

Return a short answer in this order:
1. One line saying whether the thing they want is possible on their platform and account type.
2. Numbered taps, with UI labels in bold, or the prerequisite they're missing.
3. What to ask their admin for, if the blocker is an enterprise setting.
4. A link to the matching GitHub Docs page.

## What the App Can Do

- Manage, triage, and clear notifications
- Read, review, and collaborate on issues and pull requests
- Edit files in pull requests
- Search for, browse, and interact with users, repositories, and organizations
- Get a push notification when someone mentions your username
- Search code in a specific repository (GitHub.com and GHE.com only; not available on GitHub Enterprise Server at any version)
- Secure the account with two-factor authentication and approve sign-ins from unrecognized devices (personal GitHub.com accounts only; not GitHub Enterprise Server, and not managed user accounts on GHE.com or other Enterprise Managed Users enterprises, whose MFA is set up at the identity provider)
- Ask GitHub Copilot Chat coding questions, and assign issues to Copilot (GitHub.com and GHE.com only; not GitHub Enterprise Server)

Deeper docs (all under `https://docs.github.com/en/`):

| Topic | Path |
| --- | --- |
| Mobile notifications | `subscriptions-and-notifications/get-started/configuring-notifications` |
| Code search on mobile (not GHES) | `search-github/github-code-search/using-github-code-search` |
| 2FA with GitHub Mobile (personal GitHub.com accounts) | `authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication` |
| Copilot Chat on mobile (not GHES) | `copilot/how-tos/copilot-on-github/chat-with-copilot/chat-in-mobile` |
| Assign issues to Copilot (not GHES) | `copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions` |

## Install

Point the user to https://github.com/mobile for the Android and iOS store links.

## Prerequisites by Account Type

| Account | Requirement |
| --- | --- |
| GitHub.com | None beyond the current app |
| GHE.com (data residency) | App version iOS 1.182.0+ or Android 1.178.0+ |
| GitHub Enterprise Server | App 1.4+; server 3.0+; the enterprise owner must enable mobile support. While GHES support is in public preview, the user must also be signed in with a personal GitHub.com account |

Other things to check for Enterprise Server:

- Push notifications use background fetch, so they can arrive late. That's expected, not a bug.
- If the enterprise is only reachable over VPN, the app may not work at all.
- For the admin side, see "Managing GitHub Mobile for your enterprise" in the GHES docs.

## Accounts

The app can hold several accounts at once across GitHub.com, GHE.com, and Enterprise Server.

- **Add an account:** at the bottom of the app, long-press **Profile**, tap **Add Enterprise Account**, and follow the prompts.
- **Switch accounts:** long-press **Profile**, then tap the account to switch to.
- **Sign out of one account:** long-press **Profile**, swipe left on the account, tap **Sign out**.
- **Alternative:** open the **Profile** tab, tap the gear icon, then **Manage Accounts** to add or remove accounts.

### Social login

- Google and Apple are supported on both Android and iOS.
- It only works if the GitHub account was *originally created* with that provider. If not, the user signs in with their normal GitHub credentials.
- It's only available on GitHub Free and GitHub Enterprise Cloud.

## Language

Supported: English, Spanish, Japanese, Brazilian Portuguese, Simplified Chinese, Korean, German.

The app follows the device language when it's one of these. To override it, use the app's **Settings** menu.

## iOS Universal Links

On iOS, tapping a GitHub link opens it in the app instead of Safari by default.

- **Open links in Safari instead:** long-press any GitHub link and tap **Open**. Later links for that same GitHub instance open in Safari.
- **Switch back to the app:** long-press a GitHub link and tap **Open in GitHub**.

## Leave the iOS Public Preview (TestFlight)

1. Open the TestFlight app.
2. Under "Apps", tap **GitHub**.
3. At the bottom of the page, tap **Stop Testing**.

## Feedback

Feature requests and feedback go to GitHub Community: https://github.com/orgs/community/discussions/categories/mobile

## Approval Boundaries

- This playbook takes no actions on the user's behalf. Don't change account, security, or enterprise settings for them; give the steps and let them do it.
- Don't invent menu paths. If the UI the user describes doesn't match these steps, say the app may have changed and link the official docs.
- Never ask for passwords, 2FA codes, or recovery codes.
- For enterprise policy problems (mobile disabled, VPN-only access), the fix belongs to the enterprise owner. Tell the user what to ask their admin for.
- If these steps don't match the official docs, or a version requirement may be out of date, say so and link the docs instead of guessing.
- If a managed user account (Enterprise Managed Users, including GHE.com) asks about 2FA or MFA, send them to their identity-provider administrator; they can't set it up in GitHub Mobile.
- Don't suggest upgrading GitHub Enterprise Server to get code search or Copilot on mobile; those features are cloud-only.

## Attribution

Adapted from the GitHub Docs article ["GitHub Mobile"](https://docs.github.com/en/get-started/using-github/github-mobile), © GitHub, Inc., licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Restructured as an agent playbook; wording and structure changed.
