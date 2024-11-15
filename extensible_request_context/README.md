## 📚 Description

Demonstrates a framework to manage RequestContext objects that carries context for currently handled request and allow extending request object with extensions.

## 🎯 Pros

- BaseRequestContext does not have dependencies.
- BaseRequestContext can be extended to add extra properties, that may be using optional dependencies.
- Factory is instanciated as a singleton in app using context so that it can be used from any of its components.
- Factory handles passing configuration to all extensions that need to extend context.

## 🚫 Cons

- Apps need to extend BaseRequestContext to define their own RequestContext class.
