def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["message"],
        "name": error["name"],
        "source": error["source"]
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return{
        "file_path": file_path,
        "errors": errors,
        "line": errors["line_number"],
        "column": errors["column_number"],
        "message": errors["message"],
        "name": errors["name"],
        "source": errors["source"]
    }


def format_linter_report(linter_report: dict) -> list:
    return {
        "file_path": linter_report["file_path"],
        "errors": linter_report["errors"],
        "line": linter_report["line"],
        "column": linter_report["column"],
        "message": linter_report["message"],
        "name": linter_report["name"],
        "source": linter_report["source"]
    }
