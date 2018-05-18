# Python StackOverflow Questions

Full text of questions and answers from Stack Overflow that are tagged with the python tag, useful for natural language processing and community analysis. 

## Answers

Contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.

There are some nan entries which must be removed for numeric columns to be used.

```bash
sed -i.bak 's/NA//g' Answers.csv
```

There are also some characters that won't import correctly with UTF8 and some quotations inside the text of the question. Students will have to fix them in whatever fashion is deemed appropriate.

```sql
CREATE TABLE answers (
    Id              numeric,
    OwnerUserId     numeric,
    CreationDate    varchar,
    ParentId        numeric,
    Score           numeric,
    Body            varchar);

COPY answers
FROM '/home/ubuntu/python_questions/Answers.csv'
DELIMITER ','
CSV HEADER;
```

## Tags

Contains the tags on each question besides the Python tag.

```sql
CREATE TABLE tags (
    Id     numeric,
    Tag    varchar);

COPY tags
FROM '/home/ubuntu/python_questions/Tags.csv'
DELIMITER ','
CSV HEADER;
```

## Questions

Contains the title, body, creation date, score, and owner ID for each Python question.

There are some nan entries which must be removed for numeric columns to be used.

```bash
sed -i.bak 's/NA//g' Questions.csv
```

There are also some characters that won't import correctly with UTF8 and some quotations inside the text of the question. Students will have to fix them in whatever fashion is deemed appropriate.

```sql
CREATE TABLE questions (
    Id              numeric,
    OwnerUserId     numeric,
    CreationDate    varchar,
    Score           numeric,
    Title           varchar,
    Body            varchar);

COPY questions
FROM '/home/ubuntu/python_questions/Questions.csv'
DELIMITER ','
CSV HEADER;
```