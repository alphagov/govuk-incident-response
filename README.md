# GOV.UK Incident Response

This repo is part of an investigation into how to improve GOV.UK's incident management process. It uses [Monzo's Response] tool to manage conversations on Slack and compile a report based on Slack messages.

[Monzo's Response]: https://github.com/monzo/response

## How to

### Install

```sh
$ pipenv install
```

### Run

```sh
$ pipenv run python manage.py migrate
$ pipenv run python manage.py runserver
```

### Deploy

```sh
$ pipenv lock -r > requirements.txt
$ cf push govuk-incident-response
```

Follow [the instructions](https://github.com/monzo/response#completing-the-setup-and-config-with-slack) from Monzo to set up the application in Slack. This only needs to be done once.

## Findings

I've tried to order the findings by how positive/negative it is in relation to using the tool for GOV.UK.

- **Actions can be recorded during an incident.** This saves a lot of time and avoids people dealing with an incident having to pause their work, find the incident report and type it in. Instead, since they'll already be chatting in Slack, they can @-message the bot and record an action quickly.

- **Automatically manages incident channels and notifies people.** The tool automatically creates a channel for the specific incident (allowing multiple incidents to happen at the same time) and by having a dedicated channel, we could relatively easily export all the conversations in one go.

- **Web interface allows viewing the report in real time.** The web interface acts as place to find all previous and live incident reports. This means it's all in one place and easy to find.

- **No built-in authentication scheme.** We would need to implement our own authentication schema using Django's API. We would have to decide whether to integrate it into Google, Sign On, or something else.

- **Only pinned messages are included in the report.** One of the difficult jobs of the comms lead during an incident is having to pick out the useful messages and adding them to the incident report. We thought that the tool would automatically include all messages in the report, but actually only pinned messages appear. This doesn't save much time as instead of copy and pasting, the comms lead would need to pin all the relevant messages.

- **Replies in threads are not automatically added to the report and don't appear
correctly in the timeline.** Related to the above finding, any messages part of a thread where the original message is pinned are not automatically included in the report. This means the comms lead would need to pin each message inside the thread. Once pinned, the inline messages don't appear in the report as part of a thread.

- **Messages/actions are not tagged to a name.** We're not sure if this was because we disabled authentication in our experiements, but any pinned messages and actions in the report and not labelled by who wrote it. For actions this might make it harder to discover more details about an action. At the same time, it might help towards a no blame culture.

- **Severity levels are hard-coded.** We would need to change the code of the app if we wanted to change these to better fit with GOV.UK's priority levels.

- **Had to use a fork to fix a deprecation issue with the Slack API.** There's currently [an open issue in the tool][response-issue] where it doesn't work for apps created after July 10th because Slack has deprecated some old APIs. To fix this for our experiements, we had to use a fork. This isn't necessarily a bad thing, but it might indicate something about the pace of development.

[response-issue]: https://github.com/monzo/response/pull/220
