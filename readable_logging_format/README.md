## 📚 Description

Following snippet defines custom log record formatters:

- **DebugFormatter** whose provide colored output and readable format for debugging
- **GELFFormatter** who output logs in GELF format more suitable for parsing and export in production environments

## Examples

- Using debug logging format (use colored output by default)

```log
INFO                  POST /accounts
01:54:38.023541         log_type: toto.log
                        http_status: 409
                        http_method: POST
                        http_endpoint: /accounts
                        http_path: /accounts
                        request_id: 64151abbfd354877a48513a79a38c3ee

WARNING               Cannot create account. An account already exists with email: toto@example.com
01:54:38.023609         log_type: toto.log
                        account_email: toto@example.com
```

- Using GELF logging format

```json
{"host": "laptop1515749", "level": 6, "short_message": "GET /accounts/fe8z4f8ez4f8ez", "timestamp": 1732064157.2697294, "version": "1.1", "_log_type": "toto.log", "_africa": "yolo", "_http_status": 200, "_http_method": "GET", "_http_endpoint": "/accounts/{accountId}", "_http_path": "/accounts/fe8z4f8ez4f8ez", "_request_id": "4d4ea2c13ad143bf863c3ab022266adc"}
{"host": "laptop1515749", "level": 6, "short_message": "POST /accounts", "timestamp": 1732064157.2698216, "version": "1.1", "_log_type": "toto.log", "_http_status": 409, "_http_method": "POST", "_http_endpoint": "/accounts", "_http_path": "/accounts", "_request_id": "18845dcdd5d84db0897f151a371a7f9f"}
{"host": "laptop1515749", "level": 4, "short_message": "Cannot create account. An account already exists with email: toto@example.com", "timestamp": 1732064157.26986, "version": "1.1", "_log_type": "toto.log", "_account_email": "toto@example.com"}
```
