# backend definition.
# Set this to point to your content server.

backend default {
    .host = "127.0.0.1";
    .port = "8080";
}

backend plone {
    .host = "127.0.0.1";
    .port = "8000";
}

backend fiona {
    .host = "127.0.0.1";
    .port = "8001";
}

# Below is a commented-out copy of the default VCL logic.  If you
# redefine any of these subroutines, the built-in logic will be
# appended to your code.
sub vcl_recv {
    # Purging
    if (req.request == "PURGE") {
        return(lookup);
    }

    # Backend selection
    if (req.url ~ "^/_include/") {
        set req.backend = fiona;
    } else if (req.url ~ "\.include") {
        set req.backend = plone;
        set req.http.X-Theme-Disabled = true;
        # Never Cache Plone Backend .includes
        return (pass);
    } else if (req.http.X-Backend-For == "Fiona") {
        set req.backend = fiona;
    } else if (req.http.X-Backend-For == "Plone") {
        set req.backend = plone;
    } else {
        error 500 "Unknown Backend";
    }

/*
    # All assests from the theme should be cached anonymously, also from ++plone++static
    if (req.http.Authorization || req.http.Cookie ~ "__ac" || req.http.Cookie ~ "__shibsession") {
        if (req.url !~ "(\+\+theme\+\+lmu|\+\+plone\+\+static|portal_css|portal_javascript|\+\+resource\+\+lmu)") {
            return (pass);
        } else {
          unset req.http.Authorization;
          unset req.http.Cookie;
          return (lookup);
        }
    }
*/
}

sub vcl_hit {
  if (req.request == "PURGE") {
    purge;
    error 200 "Purged.";
  }
}

sub vcl_miss {
  if (req.request == "PURGE") {
    purge;
    error 200 "Purged.";
  }
}

sub vcl_fetch {
    if (req.http.X-Use-ESI) {
       set beresp.do_esi = true;
       set beresp.ttl = 5m;
    }

    if (req.url ~ "/frontpage_view.include" ) {
        set beresp.ttl = 1m;
        set beresp.http.cache-control = "max-age=300;s-maxage=300";
        set beresp.http.max-age = "300";
        set beresp.http.s-maxage = "300";
        return ( deliver );
    }

    if (req.url ~ "/..images/" ) {
        set beresp.ttl = 5m;
        set beresp.http.cache-control = "max-age=300;s-maxage=0";
        set beresp.http.max-age = "300";
        set beresp.http.s-maxage = "0";
        return ( deliver );
    }
    if (req.url ~ "(\+\+theme\+\+lmu|\+\+plone\+\+static|portal_css|portal_javascript|\+\+resource\+\+lmu)" ) {
        set beresp.ttl = 1209600s;
        set beresp.http.cache-control = "max-age=1209600;s-maxage=1209600";
        set beresp.http.max-age = "1209600";
        set beresp.http.s-maxage = "1209600";
        return ( deliver );
    }

}
