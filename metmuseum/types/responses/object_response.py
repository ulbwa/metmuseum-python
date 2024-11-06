from datetime import datetime
from typing import Annotated

from annotated_types import Gt, MinLen
from pydantic import BaseModel, Field, field_validator

from metmuseum.types import models


class ObjectResponse(BaseModel):
    id: Annotated[int, Gt(0)] = Field(alias="objectID")
    is_highlight: bool = Field(alias="isHighlight")
    accession_number: str = Field(alias="accessionNumber")

    # str (year), str (yyyy-mm-dd), whatever found, so i can't validate this field
    accession_year: str | None = Field(alias="accessionYear")

    is_public_domain: bool = Field(alias="isPublicDomain")
    primary_image: Annotated[str, MinLen(1)] | None = Field(alias="primaryImage")
    primary_image_small: Annotated[str, MinLen(1)] | None = Field(
        alias="primaryImageSmall"
    )
    additional_images: tuple[str, ...] = Field(alias="additionalImages")
    constituents: tuple[models.ObjectConstituent, ...] | None = Field(
        alias="constituents"
    )
    department: str = Field(alias="department")
    name: Annotated[str, MinLen(1)] | None = Field(alias="objectName")
    title: Annotated[str, MinLen(1)] | None = Field(alias="title")
    culture: Annotated[str, MinLen(1)] | None = Field(alias="culture")
    period: Annotated[str, MinLen(1)] | None = Field(alias="period")
    dynasty: Annotated[str, MinLen(1)] | None = Field(alias="dynasty")
    reign: Annotated[str, MinLen(1)] | None = Field(alias="reign")
    portfolio: Annotated[str, MinLen(1)] | None = Field(alias="portfolio")
    artist_role: Annotated[str, MinLen(1)] | None = Field(alias="artistRole")
    artist_prefix: Annotated[str, MinLen(1)] | None = Field(alias="artistPrefix")
    artist_display_name: Annotated[str, MinLen(1)] | None = Field(
        alias="artistDisplayName"
    )
    artist_display_bio: Annotated[str, MinLen(1)] | None = Field(
        alias="artistDisplayBio"
    )
    artist_suffix: Annotated[str, MinLen(1)] | None = Field(alias="artistSuffix")
    artist_alpha_sort: Annotated[str, MinLen(1)] | None = Field(alias="artistAlphaSort")
    artist_nationality: Annotated[str, MinLen(1)] | None = Field(
        alias="artistNationality"
    )

    # int (year), str (yyyy-mm-dd), whatever found, so i can't validate this fields
    artist_begin_date: Annotated[str, MinLen(1)] | None = Field(alias="artistBeginDate")
    artist_end_date: Annotated[str, MinLen(1)] | None = Field(alias="artistEndDate")

    artist_gender: Annotated[str, MinLen(1)] | None = Field(alias="artistGender")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    artist_wikidata: Annotated[str, MinLen(1)] | None = Field(alias="artistWikidata_URL")
    artist_ulan: Annotated[str, MinLen(1)] | None = Field(alias="artistULAN_URL")

    date: Annotated[str, MinLen(1)] | None = Field(alias="objectDate")

    # int (year), str (yyyy-mm-dd), whatever found, so i can't validate this fields
    begin_date: str = Field(alias="objectBeginDate")
    end_date: str = Field(alias="objectEndDate")

    medium: Annotated[str, MinLen(1)] | None = Field(alias="medium")
    dimensions: Annotated[str, MinLen(1)] | None = Field(alias="dimensions")
    dimensions_parsed: tuple[models.ObjectDimensions, ...] = Field(
        alias="dimensionsParsed", default_factory=tuple
    )
    measurements: tuple[models.ObjectMeasurementsElement, ...] | None = Field(
        alias="measurements"
    )
    credit_line: Annotated[str, MinLen(1)] | None = Field(alias="creditLine")
    geography_type: Annotated[str, MinLen(1)] | None = Field(alias="geographyType")
    city: Annotated[str, MinLen(1)] | None = Field(alias="city")
    state: Annotated[str, MinLen(1)] | None = Field(alias="state")
    county: Annotated[str, MinLen(1)] | None = Field(alias="county")
    country: Annotated[str, MinLen(1)] | None = Field(alias="country")
    region: Annotated[str, MinLen(1)] | None = Field(alias="region")
    subregion: Annotated[str, MinLen(1)] | None = Field(alias="subregion")
    locale: Annotated[str, MinLen(1)] | None = Field(alias="locale")
    locus: Annotated[str, MinLen(1)] | None = Field(alias="locus")
    excavation: Annotated[str, MinLen(1)] | None = Field(alias="excavation")
    river: Annotated[str, MinLen(1)] | None = Field(alias="river")
    classification: Annotated[str, MinLen(1)] | None = Field(alias="classification")
    rights_and_reproduction: Annotated[str, MinLen(1)] | None = Field(
        alias="rightsAndReproduction"
    )
    link_resource: Annotated[str, MinLen(1)] | None = Field(alias="linkResource")
    metadata_date: datetime = Field(alias="metadataDate")
    repository: str = Field(alias="repository")

    # Should this value always contain a URL? If so, can we use AnyHttpUrl here?
    url: str = Field(alias="objectURL")

    tags: tuple[models.ObjectTag, ...] | None = Field(alias="tags")

    # I think we need to use validation with AnyHttpUrl,
    # but the API responses sometimes contain values like "(not assigned)",
    # so i can't be sure if there are other values that should also be handled as None.
    # This solution might cause issues later on
    wikidata: Annotated[str, MinLen(1)] | None = Field(alias="objectWikidata_URL")

    is_timeline_work: bool = Field(alias="isTimelineWork")
    gallery_number: Annotated[str, MinLen(1)] | None = Field(alias="GalleryNumber")

    @field_validator(
        "wikidata",
        "primary_image",
        "primary_image_small",
        "artist_wikidata",
        "artist_ulan",
        "artist_begin_date",
        "artist_end_date",
        "accession_year",
        "dynasty",
        "reign",
        "portfolio",
        "artist_prefix",
        "artist_suffix",
        "geography_type",
        "city",
        "state",
        "county",
        "country",
        "region",
        "subregion",
        "locale",
        "locus",
        "excavation",
        "river",
        "rights_and_reproduction",
        "link_resource",
        "gallery_number",
        "artist_display_name",
        "artist_display_bio",
        "culture",
        "period",
        "artist_gender",
        "classification",
        "name",
        "artist_nationality",
        "dimensions",
        "medium",
        "artist_role",
        "date",
        "artist_alpha_sort",
        "credit_line",
        "title",
        mode="before",
    )
    def validate_empty_str_as_none(cls, v: str) -> str | None:
        if v == "":
            return None
        return v

    @field_validator(
        "artist_begin_date", "artist_end_date", "begin_date", "end_date", mode="before"
    )
    def validate_int_as_str(cls, v: int | None) -> str | None:
        if v is not None:
            return str(v)
        return v


__all__ = ("ObjectResponse",)
