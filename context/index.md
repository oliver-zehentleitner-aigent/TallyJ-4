# Context index

Lean index of project *why* knowledge. Load a topic file only when the work touches that area.

## 0

## 1

## 2

## 3

## 4

## 5

## 6

## 7

## 8

## 9

## A

- [api-contracts.md](api-contracts.md) — dual API response wrappers and OpenAPI client regeneration
- [architecture.md](architecture.md) — single backend host after domain consolidation; where code lives; social preview URLs are static HTML pinned to production
- [auth.md](auth.md) — JWT identity claims (`sub` / `NameIdentifier`); teller vs online-voter cookie transport; online ballot identity is the voter session; guest teller login is rate-limited per IP and locked per election; IdP-first teller signup; SuperAdmin one-time invite for local email/password

## B

- [ballot-validation.md](ballot-validation.md) — pre-finalization integrity; count-reconciliation report before Analyze/Finalize

## C

## D

## E

- [election-analysis.md](election-analysis.md) — core analysis engine; risk-first correctness vs v3
- [election-state.md](election-state.md) — teller coordination, Finalized write lock, and #191 concurrent-teller SQLite coverage

## F

- [front-desk.md](front-desk.md) - Ballot Not Received filter; method codes (P not I); pending-online withdraw on method switch; Unregister + re-check-in while open; Finalized is registration-done; Accept-all vs check-in race; Roll Call / envelope pages not in v4

## G

## H

## I

- [i18n-rich-entries.md](i18n-rich-entries.md) — locale leaves are `{ t, s, w }`; runtime and bundles see text only; AI must not overwrite human or approved
- [i18n.md](i18n.md) — html `dir` with locale; version label is one string (Persian uses بتا); public/voter RTL vs Element Plus RTL CSS

## J

## K

- [kiosk.md](kiosk.md) — kiosk as teller-minted 15-minute codes on a shared browser; not mint-on-read

## L

## M

## N

## O

- [online-ballots.md](online-ballots.md) - Draft autosave vs Submitted, online acceptance (pending until Accept-all), reserved Online/Imported locations, monitor close countdown, anonymous ballot-page sessions, and random name resolution

## P

- [people-import.md](people-import.md) — three-action import pipeline (not a Next/Previous wizard)
- [people.md](people.md) - person fields; AgeGroup removed (eligibility is V01/X05); cannot-vote lock after accepted ballot; guest Can Add People / Name not in the List; Confidential X is a named ordinary person

## Q

## R

- [realtime.md](realtime.md) — SignalR hub group naming (not a single `election-{guid}` pattern)
- [reports.md](reports.md) — VotersByArea 18+/18–21 (V01), download-all zip of the existing report list, Front Desk vs analysis voted rule; Analyze SaveManual persists M without re-running Analyze; vote `/ tie-break` only when a count was entered

## S

- [sms-eligibility.md](sms-eligibility.md) — reject reserved/fictional/malformed phones before paid SMS/voice/WhatsApp; OnlineVoter.SmsStatus; ensure phone row on Person write; person detail phone status and recent SmsLog; Twilio callback auto-learn and delivered OK; send-side SmsLog + StatusCallback; teller manual SmsStatus; Front Desk / people list SMS hint; OnlineVoter.WhatsAppStatus (GreenAPI checkWhatsapp); People list Has WhatsApp filter

## T

- [test-elections.md](test-elections.md) — duplicate as test copy (`ShowAsTest`); teller test banner; test-only runtime reset
- [theme.md](theme.md) — dark hairlines, stage chips, name links, leftover warning/fill/inverse surfaces, branch badge, and audit muted text (#285)

## U

## V

## W

## X

## Y

## Z
