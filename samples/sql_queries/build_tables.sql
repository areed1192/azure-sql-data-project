IF Object_ID('news_articles_cnbc') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_cnbc]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [type] NVARCHAR(MAX) NULL,
    [article_id] NVARCHAR(MAX) NULL,
    [sponsored] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_cnn') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_cnn]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [thumbnail] NVARCHAR(MAX) NULL,
    [article_id] NVARCHAR(MAX) NULL,
    [sponsored] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_market_watch') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_market_watch]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [link] NVARCHAR(MAX) NULL,
    [origin_link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [article_id] NVARCHAR(MAX) NULL,
    [title] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_seeking_alpha') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_seeking_alpha]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_sp_global') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_sp_global]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [source] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_wsj') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_wsj]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [encoded] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL,
    [article_type] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_yahoo_finance') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_yahoo_finance]
(

    [news_id] NVARCHAR(60) NOT NULL,
    [news_source] NVARCHAR(60) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [text] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [content] NVARCHAR(MAX) NULL,
    [article_type] NVARCHAR(MAX) NULL,
    [source] NVARCHAR(MAX) NULL,
    [credit] NVARCHAR(MAX) NULL

);

IF Object_ID('news_articles_nasdaq') IS NULL

CREATE TABLE [stock-financials].[dbo].[news_articles_nasdaq]
(

    [news_id] NVARCHAR(MAX) NOT NULL,
    [news_source] NVARCHAR(MAX) NOT NULL,
    [title] NVARCHAR(MAX) NULL,
    [link] NVARCHAR(MAX) NULL,
    [description] NVARCHAR(MAX) NULL,
    [publication_date] NVARCHAR(MAX) NULL,
    [guid] NVARCHAR(MAX) NULL,
    [creator] NVARCHAR(MAX) NULL,
    [category] NVARCHAR(MAX) NULL,
    [tickers] NVARCHAR(MAX) NULL,
    [partner_link] NVARCHAR(MAX) NULL

);
