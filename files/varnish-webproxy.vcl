# backend definition.  Set this to point to your content
# server.
# 
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
# 
# Below is a commented-out copy of the default VCL logic.  If you
# redefine any of these subroutines, the built-in logic will be
# appended to your code.
sub vcl_recv {
    if (req.http.X-Backend-For == "Fiona") {
        set req.backend = fiona;
    } else if (req.http.X-Backend-For == "Plone") {
        set req.backend = plone;
    } else {
        error 500 "Unknown Backend";
    }

    if (req.request == "PURGE") {
        return(lookup);
    }
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
}
