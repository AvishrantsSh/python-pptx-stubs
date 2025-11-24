# python-pptx-stubs

This package contains [type stubs](https://www.python.org/dev/peps/pep-0561/) to provide more precise static types and type inference for the [python-pptx](https://github.com/scanny/python-pptx) project.

**python-pptx** heavily relies on dynamic attribute generation and runtime magic for its functionality. This project aims to add type annotations for the most common patterns used in the parent library.

> **Note:** This is **not an official package** from the python-pptx maintainers. It is a community-maintained project to provide type hints for python-pptx.

## ⚠️ Development Status

This package is under **active development** and is **not intended for production use**. Type annotations may be incomplete or change without notice.

## Installation

```bash
pip install python-pptx-stubs
```

## Compatibility

This project follows the same versioning as python-pptx where possible.

| Stubs Version | python-pptx Version | Python Version | Status  |
|---------------|---------------------|----------------|---------|
| 1.0.2.post1   | 1.0.2               | 3.12+          | Active  |

## Usage

Once installed, type checkers like mypy and PyRight will automatically discover these stubs when analyzing python-pptx code.

**Note:** You need to have python-pptx installed separately. This package only provides type information.

## Contributing

Found an issue or want to contribute?

- **Report bugs**: [Open an issue](https://github.com/AvishrantsSh/python-pptx-stubs/issues)
- **Contribute**: Pull requests are welcome! Please open an issue first to discuss proposed changes.

## License

MIT License - see [LICENSE](LICENSE) file for details
