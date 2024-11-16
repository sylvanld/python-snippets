## 📚 Description

Demonstrates how app configuration can be handled in a modular framework.

## 🎯 Pros

- Well-defined configuration structure, with strict parsing and typing
- Ability to generate config file from defaults
- App config is fully customizable
- User can directly integrate pre-defined config groups to app config

## 🚫 Cons

- Making config an injected dependency, user is responsible to instanciate manually all objects that need access to a config instance. User is now responsible to manage wiring, maintain a singleton of all these resources, etc...
